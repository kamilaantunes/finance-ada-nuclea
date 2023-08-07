def retorna_menu_principal():
    retorna_menu_principal = input("Deseja retornar ao menu principal? (s/n")

    if retorna_menu_principal == "s":
        retorna_menu = True
    elif retorna_menu_principal == "n":
        retorna_menu = False
    return  retorna_menu

def format_text():
    while True:
        nome = input("Nome: ")
        nome_formated = nome.title()
        return nome_formated


def numero_residencia():
    while True:
        residencia = input(input("Número da residência: "))
        return residencia

def name_arquivo():
    while True:
        arquivo = input("Informe o nome do arquivo à ser salvo (à exemplo: relatorio_ordem_bbas3.txt): ").strip()
        return arquivo