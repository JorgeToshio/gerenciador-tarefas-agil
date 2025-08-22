from tarefas import (
    criar_tarefa,
    listar_tarefas,
    atualizar_tarefa,
    concluir_tarefa,
    excluir_tarefa
)

def exibir_menu():
    print("\n📋 Menu de Tarefas Ágeis")
    print("1 - Criar nova tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Concluir tarefa")
    print("5 - Excluir tarefa")
    print("0 - Sair")

def executar():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            criar_tarefa(titulo, descricao)
            print("✅ Tarefa criada com sucesso!")

        elif escolha == "2":
            tarefas = listar_tarefas()
            if not tarefas:
                print("⚠️ Nenhuma tarefa cadastrada.")
            else:
                for i, t in enumerate(tarefas):
                    print(f"{i} - {t}")

        elif escolha == "3":
            indice = int(input("Número da tarefa a atualizar: "))
            novo_titulo = input("Novo título (ou Enter para manter): ")
            nova_descricao = input("Nova descrição (ou Enter para manter): ")
            tarefa = atualizar_tarefa(indice,
                                       novo_titulo if novo_titulo else None,
                                       nova_descricao if nova_descricao else None)
            if tarefa:
                print("✏️ Tarefa atualizada!")
            else:
                print("❌ Tarefa não encontrada.")

        elif escolha == "4":
            indice = int(input("Número da tarefa a concluir: "))
            tarefa = concluir_tarefa(indice)
            if tarefa:
                print("✔️ Tarefa marcada como concluída!")
            else:
                print("❌ Tarefa não encontrada.")

        elif escolha == "5":
            indice = int(input("Número da tarefa a excluir: "))
            tarefa = excluir_tarefa(indice)
            if tarefa:
                print("🗑️ Tarefa excluída!")
            else:
                print("❌ Tarefa não encontrada.")

        elif escolha == "0":
            print("👋 Saindo do gerenciador. Até mais!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()