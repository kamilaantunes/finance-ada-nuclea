import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from repository.banco_de_dados import BancoDados

def realizar_analise_carteira(cpf):
        # Conectando ao bd
    banco_dados = BancoDados()

        # Obtendo as ordens do cliente através do CPF
    ordens = banco_dados.select_ordem(cpf)

    if ordens.empty:
        print("Cliente não possui ordens registradas!")
        return

        # Definindo o período de data desejada
    start_date = "2020-01-01"
    end_date = "2023-01-01"

        # Criando um dataFrame vazio
    df = pd.DataFrame()

        # Baixar os dados para cada ação e adicionar ao dataFrame
    for ordem in ordens:
        ticker = ordem[2] + '.SA'
        cotacao = yf.download(ticker, start=start_date, end=end_date)
        df[ticker] = cotacao['Adj Close']

        # Plotar as séries de preços do dataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor ticket')
    plt.title('Variação de valores das ações')
    plt.legend()
    plt.show()

# if __name__ == "__main__":
#     main()