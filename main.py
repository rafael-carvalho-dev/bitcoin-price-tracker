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

    while True:
        # Get user inputs
        currency = get_currency_choice()
        reference_value = get_reference_value(currency)
        email = get_email()
        
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
            body = f'Preço do Bitcoin em {currencies[currency]}: {bitcoin_price}'
            recipient = email
            sleep(1)
            send_email_alert(smtp_sender, smtp_password, subject, body, recipient)
        
        sleep(600) # Wait for 10 minutes before checking again

if __name__ == '__main__':
    main()
