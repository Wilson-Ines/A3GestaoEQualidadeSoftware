from aluno import Aluno
from sistema import SistemaAlunos

def menu():
    print("\n--- Sistema de Alunos ---")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Atualizar aluno")
    print("5 - Remover aluno")
    print("6 - Sair")

def executar():
    sistema = SistemaAlunos()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                matricula = input("Matrícula: ")
                aluno = Aluno(nome, idade, matricula)
                sistema.adicionar_aluno(aluno)
                print("Aluno adicionado com sucesso.")

            elif opcao == '2':
                alunos = sistema.listar_alunos()
                if alunos:
                    for aluno in alunos:
                        print(aluno)
                else:
                    print("Nenhum aluno cadastrado.")

            elif opcao == '3':
                matricula = input("Digite a matrícula: ")
                aluno = sistema.buscar_aluno(matricula)
                print(aluno if aluno else "Aluno não encontrado.")

            elif opcao == '4':
                matricula = input("Digite a matrícula do aluno: ")
                novo_nome = input("Novo nome (pressione Enter para manter o nome já cadastrado): ")
                nova_idade = input("Nova idade (pressione Enter para manter a idade já cadastrada): ")
                idade_int = int(nova_idade) if nova_idade else None
                if sistema.atualizar_aluno(matricula, novo_nome or None, idade_int):
                    print("Aluno atualizado.")
                else:
                    print("Aluno não encontrado.")

            elif opcao == '5':
                matricula = input("Digite a matrícula do aluno: ")
                if sistema.remover_aluno(matricula):
                    print("Aluno removido.")
                else:
                    print("Aluno não encontrado.")

            elif opcao == '6':
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print(f"Erro: {e}")
