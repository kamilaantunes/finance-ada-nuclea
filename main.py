from utils.funcoes_auxiliares import retorna_menu_principal, format_text, name_arquivo, numero_residencia
from utils.valida_rg import valida_rg
from utils.valida_cpf import valida_cpf, valida_cpf_ordem
from utils.valida_cep import valida_cep
from utils.valida_data import valida_data_nascimento
from utils.functions_ordem import format_ticket, valor_compra, quantidade_compra, data_compra

from carteira import realizar_analise_carteira
from models.client import Client

from models.ordem import Ordem

clientes = []

def main():
    validador = True

    while(validador):
        print("Seja bem-vindo(a) ao Sistema de Gerenciamento de Carteira de ações da Núclea com a Ada Tech! Informe uma das opções abaixo: ")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise da carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cliente = Client()
            print("Informe os dados do cliente:")
            print("1 - Cadastrar cliente")
            print("2 - Consultar cliente")
            print("3 - Atualizar cliente")
            print("4 - Excluir cliente")
            print("5 - Retornar ao menu principal")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                new_cliente = {
                    "nome": format_text(),
                    "cpf": valida_cpf(),
                    "rg": valida_rg(),
                    "data_nascimento": valida_data_nascimento(),
                    "cep": valida_cep(),
                    "numero_residencia": numero_residencia(),
                }
                cliente.cadastrar_client(new_cliente)
            elif opcao == "2":
                cpf_consulta = valida_cpf()
                cliente.consultar_client(cpf_consulta)
            elif opcao == "3":
                cpf_update = valida_cpf()
                new_dados = {
                    "nome": format_text(),
                    "cpf": valida_cpf(),
                    "rg": valida_rg(),
                    "data_nascimento": valida_data_nascimento(),
                    "cep": valida_cep(),
                    "numero_casa": numero_residencia(),
                }
                cliente.update_client(cpf_update, new_dados)
            elif opcao == "4":
                cpf_delete = valida_cpf()
                cliente.delete_client(cpf_delete)
            elif opcao == "5":
                break
            else:
                print("Opção inválida! Informe uma nova opção.")

        elif opcao == "2":
            ordem = Ordem()

            while True:
                print("Menu ordem: ")
                print("1 - Cadastrar nova ordem")
                print("2 - Retornar ao menu principal")

                opcao_ordem = input("Digite a opção desejada: ")

                if opcao_ordem == "1":
                    print("Você está cadastrando uma nova ordem!")

                    new_ordem = {
                        "nome": format_text(),
                        "ticket": format_ticket(),
                        "valor_compra": valor_compra(),
                        "quantidade_compra": quantidade_compra(),
                        "data_compra": data_compra(),
                        "cpf_cliente": valida_cpf_ordem()
                    }
                    cliente_id = ordem.buscar_id_por_cpf(new_ordem['cpf_cliente'])
                    new_ordem['cliente_id'] = cliente_id
                    ordem.cadastrar(new_ordem)
                elif opcao_ordem == "2":
                    break
                else:
                    print("Opção inválida! Informe uma nova opção.")
        elif opcao == "3":
            pass
            # cpf = valida_cpf_ordem().strip()
            # realizar_analise_carteira(cpf)
        elif opcao == "4":
            pass
            # cpf = valida_cpf_ordem().strip()
            # arquivo = nome_arquivo().strip()
            # imprimir_relatorio_acao(cpf, arquivo)
        elif opcao == "5":
            print("Obrigada por utilizar o sistema de gerenciamento de carteira de ações Núclea com a Ada Tech. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()