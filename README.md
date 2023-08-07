# Sistema de Gerenciamento de Carteira de ações da Núclea com a Ada Tech!
<hr>

Bem-vindo ao projeto final do Módulo 02 - Python, parte integrante do curso de DevOps oferecido pela Ada Tech em parceria com a Núclea. Este projeto foi desenvolvido utilizando a linguagem de programação Python e banco de dados relacional, Postgres.

O projeto tem como objetivo principal fornecer a simulação de administração de uma carteira de ações, englobando tanto a gestão de clientes quanto o controle de ordens de compra.
<hr>

## Principais características:
1. **Cliente**
   - Permitirá que o usuário realize um CRUD com o cliente, possibilitando as opções:
      - Cadastrar clientes:
           - Campos: ID, nome, CPF (sendo validado através da biblioteca validate-docbr), RG, data de nascimento, CEP - logradouro, complemento, bairro, cidade e estados (dados retornados pela API ViaCEP) e número de residência.
      - Consultar cliente;
      - Atualizar cliente;
      - Deletar cliente.
2. **Ordem**
   - Representará uma ordem de compra de ação. Ao selecionar a opção de ordem, deverá ser exibido:
      - Cadastrar ordem de compra:
            - Campos: ID, nome, ticket, valor de compra, quantidade adquirida, data de compra e ID do cliente.
3. **Realizar análise da carteira**
   - Irá exibir ao usuário um gráfico utilizando a biblioteca **Matplotlib** contendo as informações das ações cadastradas no banco de dados.
   - Solicitação realizada através do CPF do cliente.
4. **Imprimir relatório da carteira ou consultar relatório da ação**
   - Imprimir o relatório com as informações das ações do cliente que estão armazenadas no banco de dados. O nome desse arquivo deve ser solicitado ao cliente e deve ter a extensão ".txt".
   - Oferecer ao cliente uma opção para consultar dados de qualquer ação, para que possa se informar sobre o seu status atual.
5. **Sair**
6. Testes unitários
<hr>

## Funções em desenvolvimento / não implementadas
1. Cliente
   - Update cliente.
2. Ordem
    - Update ordem;
    - Delete ordem;
    - Pesquisar ordem.
3. Imprimir relatório da carteira ou consultar relatório da ação.
4. Demais testes unitários

<hr>

## Execução do projeto
1. Clonar este repositório em sua máquina;
2. Instale as dependências necessárias:
   - Localizadas no arquivo "requirements".
   - > pip install validate-docbr requests faker psycopg2-binary yfinance matplotlib pandas
   - Execute o arquivo "main.py" para iniciar a aplicação.

<hr>

Kamila Antunes ☕