from repository.banco_de_dados import BancoDados


class Client:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.rg = None
        self.data_nascimento = None
        self.CEP = None
        self.logradouro = None
        self.Complemento = None
        self.Bairro = None
        self.Cidade = None
        self.Estado = None
        self.numero_resiencia = None
        self.banco_de_dados = BancoDados()

    def cadastrar_client(self, cliente):
        # self.cpf = input("CPF: ")
        self.banco_de_dados.insert(cliente)

    def consultar_client(self, cpf):
        clientes = self.banco_de_dados.select({"cpf": cpf})

        if clientes:
            cliente = clientes[0]   # Garantindo que irá retornar os dados do primeiro cliente encontrado no BD
            print("Cliente cadastrado na base de dados:")
            print("Nome: ", cliente[1])
            print("CPF: ", cliente[2])
            print("RG: ", cliente[3])
            print("Data de nascimento: ", cliente[4])
            print("CEP: ", cliente[5])
            print("Logradouro: ", cliente[6])
            print("Bairro: ", cliente[7])
            print("Complemento: ", cliente[8])
            print("Cidade: ", cliente[9] + "Estado: ", cliente[10])
            print("Número da residência: ", cliente[11])
        else:
            print("Cliente não registrado no sistema!")

    def update_client(self, cpf, new_dados):
        clientes = self.banco_de_dados.select({"cpf": cpf})

        if clientes:
            cliente = clientes[0]
            cliente_up: {
                "nome": cliente[1],
                "cpf": cliente[2],
                "rg": cliente[3],
                "data_nascimento": cliente[4],
                "endereco": {
                    "CEP": cliente[5],
                    "Logradouro": cliente[6],
                    "Complemento": cliente[7],
                    "Bairro": cliente[8],
                    "Cidade": cliente[9],
                    "Estado": cliente[10],
                },
                "numero_residencia": cliente[11]
            }
            # FINALIZAR FUCTION UPDATE

    def delete_client(self, cpf):
        cliente = self.banco_de_dados.select({"cpf": cpf})
        if cliente:
            self.banco_de_dados.delete({"cpf": cpf})
        else:
            print("Cliente não registrado no sistema!")

    def search_id_cpf(self, cpf):
        cliente_id = self.banco_de_dados.search_id_cpf(cpf)

        return cliente_id