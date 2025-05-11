# Sistema de Gerenciamento de Alunos - Código Legado

alunos = []

def adicionar_aluno(nome, idade, matricula):
    aluno = {"nome": nome, "idade": idade, "matricula": matricula}
    alunos.append(aluno)

def listar_alunos():
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")

def buscar_aluno(matricula):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

def remover_aluno(matricula):
    global alunos
    alunos = [aluno for aluno in alunos if aluno['matricula'] != matricula]

def atualizar_idade(matricula, nova_idade):
    aluno = buscar_aluno(matricula)
    if aluno:
        aluno['idade'] = nova_idade

def atualizar_nome(matricula, novo_nome):
    aluno = buscar_aluno(matricula)
    if aluno:
        aluno['nome'] = novo_nome

def contar_alunos():
    return len(alunos)

def listar_alunos_por_idade(idade_minima):
    for aluno in alunos:
        if aluno['idade'] >= idade_minima:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")

def matriculas_existentes(): 
    return [aluno['matricula'] for aluno in alunos]

def salvar_alunos_em_arquivo():
    with open('alunos.txt', 'w') as f:
        for aluno in alunos:
            f.write(f"{aluno['nome']},{aluno['idade']},{aluno['matricula']}\n")

def carregar_alunos_de_arquivo():
    global alunos
    try:
        with open('alunos.txt', 'r') as f:
            for linha in f:
                nome, idade, matricula = linha.strip().split(',')
                adicionar_aluno(nome, int(idade), matricula)
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")

def ordenar_alunos_por_nome():
    alunos.sort(key=lambda aluno: aluno['nome'])

def buscar_aluno_por_nome(nome):
    return [aluno for aluno in alunos if nome.lower() in aluno['nome'].lower()]


# Função mal planejada
def exibir_relatorio():
    print("=== RELATÓRIO DE ALUNOS ===")
    listar_alunos()
    print("===========================")

def aluno_existe(matricula):
    return any(aluno['matricula'] == matricula for aluno in alunos)

def alunos_maiores_de_idade():
    return [aluno for aluno in alunos if aluno['idade'] >= 18]

def limpar_lista_alunos():
    global alunos
    alunos = []

def mostrar_detalhes_de_um_aluno(matricula):
    aluno = buscar_aluno(matricula)
    if aluno:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Matrícula: {aluno['matricula']}")
    else:
        print("Aluno não encontrado.")

# Algumas funções desnecessárias
def listar_todos_os_nomes():
    for aluno in alunos:
        print(aluno['nome'])

def listar_todas_as_matriculas():
    for aluno in alunos:
        print(aluno['matricula'])

def listar_todas_as_idades():
    for aluno in alunos:
        print(aluno['idade'])

def inicializar_alunos_teste():
    adicionar_aluno("João", 15, "A001")
    adicionar_aluno("Maria", 14, "A002")
    adicionar_aluno("Pedro", 16, "A003")
    adicionar_aluno("Ana", 17, "A004")
    adicionar_aluno("Lucas", 18, "A005")
    adicionar_aluno("Larissa", 19, "A006")

def mostrar_detalhes_de_um_aluno(matricula):
    aluno = buscar_aluno(matricula)
    if aluno:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Matrícula: {aluno['matricula']}")
    else:
        print("Aluno não encontrado.")

def aluno_mais_velho():
    if alunos:
        mais_velho = alunos[0]
        for aluno in alunos:
            if aluno['idade'] > mais_velho['idade']:
                mais_velho = aluno
        return mais_velho
    return None

# Código principal
inicializar_alunos_teste()

listar_alunos()

print(buscar_aluno("A001"))

remover_aluno("A001")

listar_alunos()

print("Total de alunos:", contar_alunos())

atualizar_idade("A002", 15)
atualizar_nome("A003", "Pedro Silva")

listar_alunos()

print("Alunos com 15 anos ou mais:")
listar_alunos_por_idade(15)

print("Matrículas existentes:")
print(matriculas_existentes())

print("Salvando alunos em arquivo...")
salvar_alunos_em_arquivo()

print("Ordenando alunos por nome...")
ordenar_alunos_por_nome()

listar_alunos()

print("Alunos maiores de idade:")
for aluno in alunos_maiores_de_idade():
    print(aluno)

print("Buscando aluno por nome 'Ana':")
print(buscar_aluno_por_nome("Ana"))

print("Aluno mais velho:")
print(aluno_mais_velho())
