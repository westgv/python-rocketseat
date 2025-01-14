#desafio 01 rocket seat
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favorito):
    contato = {"Nome":nome_contato, "Telefone": telefone_contato, "Email": email_contato, "Favorito":favorito}
    contatos.append(contato)
    if contato["Favorito"] == True:
        contatos_favoritos.append(contato)
    print("Contato adicionado com sucesso!")

def visualizar_contatos(contatos):
    print("Contatos da minha lista\n")

    for indice, contato in enumerate(contatos, start=1):
        status = "x" if contato["Favorito"] == True else " "
        nome_contato = contato["Nome"]
        print(f'{indice}. {nome_contato} [{status}]')

def ver_mais(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato == 0:
        print("Voltando...")
    elif indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        nome = contatos[indice_contato_ajustado]["Nome"]
        telefone = contatos[indice_contato_ajustado]["Telefone"]
        email = contatos[indice_contato_ajustado]["Email"]
        favorito = 'Sim' if contatos[indice_contato_ajustado]["Favorito"] == True else 'Não'
        print(f'--- {nome} ---\nTelefone: {telefone}\nEmail: {email}\nFavorito: {favorito}')
    else:
        print('Indice de contato inválido.')
    return

def atualizar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    contatos[indice_contato_ajustado]["Nome"] = input("Digite o nome desejado: ")
    contatos[indice_contato_ajustado]["Telefone"] = input("Digite o telefone desejado: ")
    contatos[indice_contato_ajustado]["Email"] = input("Digite o email desejado: ")
    print('Contato Atualizado!')
    visualizar_contatos(contatos)

def favoritar(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if contatos[indice_contato_ajustado]["Favorito"]:
        contatos[indice_contato_ajustado]["Favorito"] = False
    else:
        contatos[indice_contato_ajustado]["Favorito"] = True
    visualizar_contatos(contatos)

def visualizar_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status = "x" if contato["Favorito"] == True else " "
        nome_contato = contato["Nome"]
        if status == "x":
            print(f'{indice}. {nome_contato} [{status}]')
            

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    contatos.remove(contatos[indice_contato_ajustado])
    



print('''Lista de contatos''')
escolha = int(input("1. Iniciar\n2. Sair\nOpção: "))
contatos = []
contatos_favoritos = []
while True:
    print('''\nContatos\n1. Adicionar Contato\n2. Visualizar Contatos\n3. Editar Contato\n4. Favoritar Contato\n5. Visualizar Favoritos\n6. Apagar Contato\n7. Sair''')
    opcao = int(input("Digite a operação desejada: "))
    
    if opcao == 1:
        print("Informe os dados do contato\n")
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        favorito = input("Deseja favoritar? (s/n)")
        fav = True if favorito.lower() == "s" else False
        adicionar_contato(contatos, nome, telefone, email, fav)
    elif opcao == 2:
        visualizar_contatos(contatos)
        if len(contatos) == 0:
            print("Nenhum contato encontrado.")
        else:
            indice_contato = int(input("Digite o indice do contato para ver mais informações ou digite 0 para voltar: "))
            ver_mais(contatos, indice_contato)
    elif opcao == 3:
        visualizar_contatos(contatos)
        indice_contato = int(input("Digite o indice do contato desejado para edição: "))
        atualizar_contato(contatos, indice_contato)
    elif opcao == 4:
        visualizar_contatos(contatos)
        indice_contato = int(input("Digite o indice do contato que deseja favoritar ou desfavoritar: "))
        favoritar(contatos, indice_contato)
    elif opcao == 5:
        visualizar_favoritos(contatos)
        indice_contato = int(input("Digite o indice do contato para ver mais informações ou digite 0 para voltar: "))
        ver_mais(contatos, indice_contato)
    elif opcao == 6:
        visualizar_contatos(contatos)
        indice_contato = int(input("Digite o indice do contato que deseja apagar: "))
        apagar_contato(contatos, indice_contato)
    elif opcao == 7:
        break

    