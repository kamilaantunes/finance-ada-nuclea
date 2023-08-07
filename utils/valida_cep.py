import requests

def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url).json()

    return response

def valida_cep():
    while True:
        cep_input = input("Informe o CEP: ")

        if cep_input.isdigit() and len(cep_input) == 8:
            response = busca_cep(cep_input)

            if "erro" not in response:
                endereco = {
                    "CEP": response.get('cep'),
                    "Logradouro": response.get('logradouro'),
                    "Complemento": response.get('complemento'),
                    "Bairro": response.get('bairro'),
                    "Cidade": response.get('localidade'),
                    "Estado": response.get('uf')
                }
                return endereco
        else:
            print("CEP não encontrado ou inválido! Informe novamente.")

if __name__ == "__main__":
    valida_cep()