def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "x" if tarefa["completada"] else " "
        nome_tarefa = tarefa['tarefa']
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado > len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else:
        print('Indice de tarefa inválido.')
    return

def completar_tarefas(tarefas, indice_tarefa):
    indice_tarefa_atualizado = indice_tarefa - 1
    tarefas[indice_tarefa_atualizado]["completada"] = True
    print(f'Tarefa {indice_tarefa} completada com sucesso!')
    return

def deletar_tarefas_completadas(tarefas):
    print('\nTarefas completadas foram excluidas.')
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefa.remove(tarefa)
    return


tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print('''\n1. Adicionar tarefa\n2. Ver tarefa\n3. Atualizar Tarefa\n4. Completar tarefa\n5. Deletar tarefas completas\n6. Sair''')
    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefas(tarefas, nome_tarefa)
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o numero da tarefa que deseja atualizar: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == 4:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o numero da tarefa que deseja completar: "))
        completar_tarefas(tarefas, indice_tarefa)
    elif escolha == 5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == 6:
        break
        


    