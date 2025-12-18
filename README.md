# automacao_olx
Projeto de automação de testes mobile para o aplicativo OLX, desenvolvido como parte da Atividade 2 da disciplina de Tópicos Especiais em Sistemas I.

### Descrição da Atividade

> Utilizando as ferramentas abordadas na aula de testes mobile* para fazer automação de testes, escolha um aplicativo existente na loja de aplicativos** e realize automação de 2 cenários de testes mobile de no mínimo 2 funcionalidades.
>
> \* ou a ferramenta que você tiver melhor afinidade para automação mobile
> \*\* especifique 2 cenarios de testes para cada funcionalidade

## Ferramentas Utilizadas

- **Linguagem:** Python
- **Framework de Automação:** Appium
- **Driver:** Appium-Python-Client
- **Test Runner:** Unittest

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python 3.11](https://www.python.org/downloads/)
- [Node.js e npm](https://nodejs.org/en/)
- [Appium Server](https://appium.io/docs/en/about-appium/getting-started/): `npm install -g appium`
- Appium Doctor: `npm install -g appium-doctor` para verificar a instalação.
- Android Studio (para o Android SDK e emulador)

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/alealmeida31/automacao_olx.git
   cd automacao_olx
   ```
2. Crie a venv e ative
   ```sh
   python3.11 -m venv .venv - MAC
   source .venv/bin/activate - MAC

   python -m venv .venv - Windows
   .venv\Scripts\Activate.ps1 - Windows
   ```
3. Installe o Appium Client
   ```sh
   pip install pytest Appium-Python-Client
   ```
4. Instale as dependências do Python:
   ```sh
   pip install -r requirements.txt
   ```
## Executando os Testes

1. Inicie o servidor Appium em um terminal:
   ```sh
   appium
   ```
2. Certifique-se de que um emulador Android esteja em execução ou um dispositivo físico esteja conectado.
3. Execute os testes a partir do diretório raiz do projeto:
   ```sh
   python -m unittest automacao_olx.py
   ```