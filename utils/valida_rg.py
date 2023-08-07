import re

def valida_rg():
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        rg = input("RG: ")

        if re.match(padrao_rg, rg):
            return True
        else:
            print("CPF inválido! Digite novamente.")

if __name__ == "__main__":
    valida_rg()