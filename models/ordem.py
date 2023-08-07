from models.client import Client
from repository.banco_de_dados import BancoDados

class Ordem:
    def __init__(self):
        self.banco_de_dados = BancoDados()
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.id_cliente = None

    def cadastrar_ordem(self, ordem):
        id_client = self.search_id_client(ordem['cpf_client'])

        if id_client is not None:
            ordem['id_client'] = id_client
            self.banco_de_dados.insert_ordem(ordem)

            print("Ordem cadastrada com êxito!\n")
        else:
            print("Cliente não encontrado, não sendo possível cadastrar a ordem. Tente novamente!")

    def consultar_ordem(self, ticket):
        ordem = self.banco_de_dados.select_ordem(ticket)

        if ordem:
            print("Ordem localizada!")
            print("Nome: ", ordem[0]['nome'])
            print("Ticket: ", ordem[1])['ticket']
            print("Valor da compra: ", ordem[2]['valor_compra'])
            print("Quantidade adquirida: ", ordem[3]['quantidade_compra'])
            print("Data da compra: ", ordem[4]['data_compra'])
            print("Cliente vinculado: ", ordem[5]['cliente_id'])
        else:
            print("Ordem não encontrada.")