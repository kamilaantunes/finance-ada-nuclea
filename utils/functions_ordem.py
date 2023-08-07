from datetime import datetime

def format_ticket():
    while True:
        nome = input("Ticket: ")
        nome_formated = nome.upper()

        return nome_formated

def valor_compra():
    while True:
        valor_compra = float(input("Valor da compra: R$ "))

        return valor_compra

def quantidade_compra():
    while True:
        quantidade_compra = int(input("Quantidade adquirida: "))

        return quantidade_compra

def data_compra():
    while True:
        data = input("Data de aquisição: ")

        try:
            data_converted = datetime.strptime(data, "%d/%m/%y").date()
            data_atual = datetime.now().date()

            if data_converted > data_atual:
                print("A data de aquisição das ordens não pode ser superior a data atual!")
            else:
                return data_converted.strftime("%d/%m/%Y")
        except ValueError as e:
            print("Erro na operação! Digite novamente a data de aquisição das ordens seguindo o formato: dia/mês/ano.")
