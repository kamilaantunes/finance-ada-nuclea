from datetime import datetime

def valida_data_nascimento():
    while True:
        data_nascimento = input("Data de nascimento: ")

        try:
            data_converted = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_converted < data_atual:
                return data_converted.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual!")
        except ValueError as e:
            print("Error and exception! " + str(e) + "Digite novamente a data de nascimento.")

if __name__ == "__main__":
    valida_data_nascimento()()