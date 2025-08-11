# 🛠️ Bot de Abertura de Chamados com Selenium

Este projeto é um bot que desenvolvi em Python utilizando a biblioteca **Selenium** para automatizar o processo de abertura de chamados.

## 🚀 Funcionalidades

- Puxa do arquivo `patri.txt` os patrimônios necessarios para o chamado
- Login automático na plataforma
- Navegação até a página de abertura de chamados
- Preenchimento automático dos campos necessários
- Envio do chamado

## 🧰 Tecnologias Utilizadas

- Python (Linguagem principal) 
- Selenium (Biblioteca de automação web)
- Google Chrome ou outro navegador compatível

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/eusejo/Bot-SDESK.git
   cd Bot-SDESK
   ```

2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Como Usar

1. Configure as variáveis de ambiante com a biblioteca `doteenv` e criando o arquivo `.env` ou diretamente no script.
2. Não esqueça de colocar os patrimônios no arquivo `patri.txt`
3. Execute o bot:
   ```bash
   python bot_chamados.py (argv1)[tipo do chamado] (argv2)[tipo do equipamento]
   ```
