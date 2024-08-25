import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pycoingecko import CoinGeckoAPI
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from time import sleep

# List of available currencies
currencies = {
    'USD': 'Dólar Americano',
    'EUR': 'Euro',
    'GBP': 'Libra Esterlina Britânica',
    'BRL': 'Real do Brasil',
    'TWD': 'Novo Dólar Taiwanês',
    'KRW': 'Won Sul-Coreano',
    'JPY': 'Iene japonês',
    'RUB': 'Rublo Russo',
    'CNY': 'Yuan chinês',
    'AUD': 'Dólar Australiano',
    'CAD': 'Dólar Canadense',
    'IDR': 'Rúpia Indonésia'
}

def instructions():
    """
    Displays the title and instructions for the Bitcoin price tracker using the Rich library.
    """
    console = Console()
    title = 'RASTREADOR DE PREÇOS DE BITCOIN'
    title_text = Text(title, justify='center', style='bold deep_sky_blue1')
    panel = Panel(title_text, title_align='center', expand=True, border_style='green')
    console.print(panel)
    sleep(1)

    console.rule('[bold bright_red]INSTRUÇÕES', align='center') # Displaying instructions panel
    sleep(1)

    text ='\nEste é um rastreador de preços de Bitcoin. Uma moeda válida e um valor de referência ou limite precisam ser definidos. Também é necessário um endereço de e-mail válido e, sempre que o preço ficar abaixo do valor esperado, um relatório será enviado por e-mail informando-o sobre o valor encontrado.'
    intro_text = Text(text, justify='full', style='bold grey74')
    console.print(intro_text)
    console.print('\n')
    sleep(10)


def get_currency_choice():
    """
    Displays available currencies and prompts the user to select one.
    
    Returns:
        str: The selected currency code.
    """
    print('Moedas disponíveis:')
    sleep(2)

    for i, (code, name) in enumerate(currencies.items()): # List all currencies
        print(f'{i+1}. {code} ({name})')

    while True:
        choice = input('Escolha uma moeda: ').upper() # Prompt user to select a currency
        if choice in [code.upper() for code in currencies]:
            return choice
        print('Escolha inválida. Por favor, escolha uma moeda válida.')


def get_reference_value(currency):
    """
    Prompts the user to input a reference value in the chosen currency.

    Args:
        currency (str): The currency code selected by the user.

    Returns:
        float: The reference value entered by the user.
    """
    while True:
        try:
            reference_value = float(input(f'Insira um valor de referência em {currencies[currency]}: '))
            if reference_value <= 0:
                print('Valor inválido. Digite um valor positivo.')
            else:
                return reference_value
        except ValueError:
            print('Valor inválido. Digite um número válido.')


def get_email():
    """
    Prompts the user to input a recipient email address.

    Returns:
        str: The email address entered by the user.
    """
    while True:
        email_address = input('Insira o e-mail destinatário: ')
        if '@' in email_address and '.' in email_address:
            return email_address
        print('E-mail inválido. Digite um e-mail válido.')


def get_bitcoin_price(currency):
    """
    Fetches the current Bitcoin price in the specified currency using the CoinGecko API.

    Args:
        currency (str): The currency code in which to fetch the Bitcoin price.

    Returns:
        float: The current Bitcoin price in the specified currency.
    """
    cg = CoinGeckoAPI()
    bitcoin_price = cg.get_price(ids='bitcoin', vs_currencies=currency)
    return float(list(bitcoin_price['bitcoin'].values())[0])


def send_email_alert(sender, sender_password, subject, body, recipient):
    """
    Sends an email alert with the specified subject and body to the recipient.

    Args:
        subject (str): The subject of the email.
        body (str): The body content of the email.
        recipient (str): The recipient email address.
        smtp_sender (str): The sender email address.
        smtp_password (str): The password for the sender email account.
    """
    # SMTP server configuration
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587  # Standard port for TLS
    smtp_sender = sender
    smtp_password = sender_password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start secure connection
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, recipient, msg.as_string())
        print(f'E-mail enviado para {recipient} com sucesso!')

    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
    finally:
        server.quit()


def menu():
    print('\nMenu:')
    print('1. Alterar Moeda')
    print('2. Alterar Valor de Referência')
    print('3. Alterar E-mail')
    print('4. Sair')
    print('5. Manter configuração atual e prosseguir com o monitoramento')
    
    while True:
        choice = input('Escolha uma opção: ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print('Escolha inválida. Por favor, escolha uma opção válida.')
