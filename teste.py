# ========================
#  Sistema TO-DO via Prompt
# ========================

todolist = []


def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        "descricao": descricao,
        "status": "pendente"
    }
    todolist.append(tarefa)
    print("✔ Tarefa adicionada com sucesso!\n")


def listar_tarefas():
    if not todolist:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n===== LISTA DE TAREFAS =====")
    for i, tarefa in enumerate(todolist):
        print(f"{i+1}. {tarefa['descricao']} - {tarefa['status']}")
    print()


def concluir_tarefa():
    listar_tarefas()
    if not todolist:
        return

    try:
        indice = int(input("Número da tarefa para concluir: ")) - 1
        todolist[indice]["status"] = "concluída"
        print("✔ Tarefa marcada como concluída!\n")
    except:
        print("⚠ Número inválido!\n")


def editar_tarefa():
    listar_tarefas()
    if not todolist:
        return

    try:
        indice = int(input("Número da tarefa para editar: ")) - 1
        nova_desc = input("Nova descrição: ")
        todolist[indice]["descricao"] = nova_desc
        print("✔ Tarefa editada com sucesso!\n")
    except:
        print("⚠ Número inválido!\n")


def remover_tarefa():
    listar_tarefas()
    if not todolist:
        return

    try:
        indice = int(input("Número da tarefa para remover: ")) - 1
        todolist.pop(indice)
        print("✔ Tarefa removida!\n")
    except:
        print("⚠ Número inválido!\n")


def menu():
    while True:
        print("===== MENU TO-DO =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar como concluída")
        print("4. Editar tarefa")
        print("5. Remover tarefa")
        print("6. Sair")
        print("======================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            editar_tarefa()
        elif opcao == "5":
            remover_tarefa()
        elif opcao == "6":
            print("Saindo do sistema... Até mais!")
            break
        else:
            print("⚠ Opção inválida! Tente novamente.\n")


# Iniciar sistema
menu()

