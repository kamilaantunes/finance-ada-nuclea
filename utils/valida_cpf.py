from validate_docbr import CPF

def valida_cpf():
    cpf_validador = CPF()

    while True:
        cpf = input("CPF: ")
        result_validacao = cpf_validador.validate(cpf)

        if (result_validacao):
            cpf_formated = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

            return cpf_formated
        else:
            print("CPF inválido! Digite novamente: ")

# def gera_cpf():
#     cpf = CPF()
#     cpf_gerado = cpf.generate()
#
#     return cpf_gerado

def valida_cpf_ordem():
    cpf_validador = CPF()

    while True:
        cpf = input("Digite o CPF do titular: ")
        cpf = ''.join(filter(str.isdigit, cpf))

        result_validation = cpf_validador.validate(cpf)

        if (result_validation):
            cpf_formated = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

            return cpf_formated
        else:
            print("CPF inválido! Digite novamente.")