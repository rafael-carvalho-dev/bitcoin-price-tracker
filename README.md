# Bitcoin Price Tracker / Rastreador de Preços de Bitcoin

## Overview / Visão Geral

Bitcoin Price Tracker is a Python-based application that tracks the price of Bitcoin in various currencies and sends an email alert if the price falls below a user-defined threshold.

Rastreador de Preço de Bitcoin é uma aplicação em Python que rastreia o preço do Bitcoin em várias moedas e envia um alerta por e-mail se o preço cair abaixo de um limite definido pelo usuário.

## Features / Funcionalidades

- Supports multiple currencies (USD, EUR, BRL, etc.)
- Sends an email alert when the Bitcoin price drops below the specified value
- User-friendly console interface with instructions

- Suporta várias moedas (USD, EUR, BRL, etc.)
- Envia um alerta por e-mail quando o preço do Bitcoin cai abaixo do valor especificado
- Interface amigável no console com instruções

## Requirements / Requisitos

- Python 3.8+
- See `requirements.txt` for a complete list of dependencies

- Veja `requirements.txt` para uma lista completa de dependências

## Installation / Instalação

1. **Clone the repository / Clone o repositório:**
   git clone https://github.com/rafael-carvalho-dev/bitcoin-price-tracker.git
   cd bitcoin-price-tracker

2. **Install the required Python packages / Instale os pacotes Python necessários:**
    pip install -r requirements.txt

3. **Set up environment variables: Create a .env file in the root directory and add your email credentials:**

**Configure as variáveis de ambiente: Crie um arquivo .env no diretório raiz e adicione suas credenciais de e-mail:**
    SMTP_SENDER=your_email@example.com
    SMTP_PASSWORD=your_email_password

## Usage / Uso

1. **Run the main.py script / Execute o script main.py**

1.1 **For Windows systems, run / Para sistema Windows, execute:**
    python main.py

1.2 **For Linux and Mac systems, run / Para sistemas Linux e Mac, execute:**
    python3 main.py

3. **Follow the on-screen instructions to select a currency, set a reference value, and enter your email address.**

**Siga as instruções na tela para selecionar uma moeda, definir um valor de referência e inserir seu endereço de e-mail.**

3. **The application will periodically check the Bitcoin price and send an alert if the price drops below the threshold.**

**O aplicativo verificará periodicamente o preço do Bitcoin e enviará um alerta se o preço cair abaixo do limite.**

## License / Licença

This project is licensed under the MIT License - see the LICENSE file for details.

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
