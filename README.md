# Interface Gráfica com Consulta de MACs

Este projeto é uma aplicação de interface gráfica construída com a biblioteca `customtkinter`, permitindo ao usuário inserir e consultar o endereço MAC de produtos WI-FI INTELBRAS. A interface exibe informações sobre o status de conexão, a versão do firmware, e o cliente associado.

## Funcionalidades

- **Criação de Cards**: A interface exibe 10 cartões (cards), cada um com campos de entrada para inserção de endereços MAC e exibição de informações do produto.
- **Consulta Automática de MAC**: Cada campo de entrada é monitorado e, ao inserir um MAC válido (12 caracteres), uma consulta é feita utilizando a função `consulta_mac`, que retorna o status do dispositivo, a versão do firmware e o cliente associado.
- **Atualização em Tempo Real**: As informações são atualizadas em tempo real a cada 2 segundos, exibindo o status atual do dispositivo.
- **Botões de Configuração e Limpeza**: A interface também possui botões para abrir uma nova janela de configuração e limpar os campos de entrada.

## Estrutura do Código

- **`create_card`**: Função responsável por criar os elementos visuais (cards) que contêm os campos de entrada e rótulos de status.
- **`update_status_async`**: Função assíncrona que realiza a consulta do MAC e atualiza o status de conexão, versão do firmware e cliente.
- **`start_async_loop`**: Inicia a execução de consultas assíncronas em uma thread separada para cada entrada de MAC.
- **`clear_entries`**: Limpa todos os campos de entrada.

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **CustomTkinter**: Biblioteca para criar interfaces gráficas com tema moderno e personalizável.
- **Asyncio**: Para realizar consultas de forma assíncrona.
- **Threading**: Para garantir que cada consulta assíncrona funcione independentemente em paralelo.

## Requisitos

Para rodar o projeto, você precisará instalar as seguintes dependências:

```bash
pip install customtkinter

Além disso, o código depende de duas funções personalizadas que você deve fornecer:

    consulta_mac: Função para realizar a consulta de dados de dispositivos com base no endereço MAC.
    open_new_window: Função que abre uma nova janela de configuração.

Como Rodar

    Clone este repositório.
    Instale as dependências necessárias.
    Execute o script principal:

bash

python main.py

Estrutura de Arquivos

bash

.
├── API/
│   └── consulta.py  # Função de consulta do MAC
├── screen/
│   └── config.py    # Função para abrir nova janela de configuração
└── main.py          # Código principal da interface

Personalização

Você pode ajustar os seguintes aspectos para adaptar a interface às suas necessidades:

    Título dos Cards: O título dos cartões pode ser personalizado na criação dos cards na função create_card.
    Cor e Estilo: O tema da interface pode ser alterado configurando o set_appearance_mode e set_default_color_theme.
    Consulta de MAC: A função consulta_mac deve ser personalizada para retornar dados reais do dispositivo.

Contato

Se tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para abrir uma issue ou entrar em contato com o autor do projeto.