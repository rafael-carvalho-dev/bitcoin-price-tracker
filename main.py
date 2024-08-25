import os
from dotenv import load_dotenv
from src import *

def main():
    """
    Main function to run the Bitcoin price tracker.
    This function continuously checks the Bitcoin price and sends an email alert
    if the price falls below the user-defined reference value.
    """
    load_dotenv() # Load SMTP credentials from environment variables

    smtp_sender = os.getenv('SMTP_SENDER')
    smtp_password = os.getenv('SMTP_PASSWORD')

    instructions() # Display instructions to the user

     # Get user inputs
    currency = get_currency_choice()
    reference_value = get_reference_value(currency)
    email = get_email()
    
    while True:
        # Fetch the current Bitcoin price
        try:
            bitcoin_price = get_bitcoin_price(currency)
        except Exception as e:
            print(f'Error fetching Bitcoin price: {e}')
            continue

        # Display the current settings
        print(f'\nValor de referência: {reference_value} {currencies[currency]}')
        print(f'Preço do Bitcoin em {currencies[currency]}: {bitcoin_price}\n')

        # Check if the Bitcoin price is below the reference value
        if bitcoin_price < reference_value:
            subject = 'Alerta de Preço do Bitcoin'
            body = f'Preço do Bitcoin abaixo do valor solicitado. Está cotado em {currencies[currency]}: {bitcoin_price}'
            recipient = email
            sleep(1)
            send_email_alert(smtp_sender, smtp_password, subject, body, recipient)

        # Clear the console
        sleep(5) # Wait...
        os.system('cls' if os.name == 'nt' else 'clear')

        # Verification alert
        print('Por favor, aguarde enquanto realizamos uma nova verificação...\n')
        
        sleep(600) # Wait for 10 minutes before checking again

        # Displays the menu to the user after each check
        choice = menu()

        if choice == '1':
            currency = get_currency_choice()
        elif choice == '2':
            reference_value = get_reference_value(currency)
        elif choice == '3':
            email = get_email()
        elif choice == '4':
            print('Saindo do programa...')
            break
        elif choice == '5':
            print('Continuando monitoramento...')


if __name__ == '__main__':
    main()
