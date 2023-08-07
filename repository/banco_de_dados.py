import psycopg2
import os

class BancoDados:
    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())      # Gerando conexão
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()


    def insert(self, cliente):
        print("Inserindo cliente no banco de dados: ")

        insert_query = """
                INSERT INTO public.cliente(
                    nome, cpf, rg, data_nascimento, cep, logradouro, complemento, bairro, cidade, estado, numero_residencia
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                );
            """

        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['cep']['CEP'],
            cliente['cep']['Logradouro'],
            cliente['cep']['Complemento'],
            cliente['cep']['Bairro'],
            cliente['cep']['Cidade'],
            cliente['cep']['Estado'],
            cliente['numero_residencia']
        )

        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cliente):
        print("Selecionando cliente no banco de dados: ")

        select_query = "SELECT * FROM CLIENTE where cpf = '" + cliente['cpf'] + "';"    # Retornando cliente de acordo com o CPF
        self.cursor.execute(select_query, (cliente['cpf'],))

        clientes = self.cursor.fetchall()

        return clientes

    def delete(self, cliente):
        print("Excluindo cliente do banco de dados!")
        delete_query = "DELETE FROM cliente WHERE cpf = %s"
        self.cursor.execute(delete_query, (cliente['cpf'],))
        self.connection.commit()

        print("Cliente excluído com sucesso!")

    def insert_ordem(self, ordem):
        print("Inserindo ordem na base de dados!")
        insert_query = """
            INSERT INTO ordem(
	            nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id
	        )
	        VALUES (
	            %s, %s, %s, %s, %s, %s
	        )
        """

        values = (
            ordem['nome'],
            ordem['ticket'],
            ordem['valor_compra'],
            ordem['quantidade_compra'],
            ordem['data_compra'],
            ordem['cliente_id']
        )

        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select_ordem(self, cpf):
        select_query = """
            SELECT ordem * FROM ordem
            JOIN cliente ON ordem.cliente_id = cliente_id
            WHERE cliente.cpf = %s
        """

        self.cursor.execute(select_query, (cpf,))
        ordens = self.cursor.fetchall()
        print(ordens)

        return ordens

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv("user"),
            "password": os.getenv("password"),
            "host": os.getenv("host"),
            "port": os.getenv("port"),
            "database": os.getenv("database")
        }

        return parametros_conexao