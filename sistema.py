import json
import os 
from aluno import Aluno 

class SistemaAlunos:
    def __init__(self, arquivo_dados="dados/alunos.json"):
        self.alunos = []
        self.arquivo_dados = arquivo_dados
        self.carregar_dados()

    def adicionar_aluno(self, aluno):
        if self.buscar_aluno(aluno.matricula):
            raise ValueError("Matrícula já cadastrada")
        self.alunos.append(aluno)
        self.salvar_dados()

    def listar_alunos(self):
        return self.alunos
    
    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
            
        return None
    
    def remover_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            self.alunos.remove(aluno)
            self.salvar_dados()
            return True
        return False
    
    def atualizar_aluno(self, matricula, novo_nome=None, nova_idade=None):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            if novo_nome:
                aluno.nome = novo_nome
            if nova_idade:
                aluno.idade =  nova_idade
            self.salvar_dados()
            return True
        return False
    
    def salvar_dados(self):
        with open(self.arquivo_dados, "w", encoding='utf-8') as f:
            json.dump([aluno.to_dict() for aluno in self.alunos], f, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', enconding= 'utf-8') as f:
                    dados = json.load(f)
                    self.alunos = [Aluno(**aluno) for aluno in dados]
            except Exception as e:
                print(f"Erro ao carregar dados: {e}")
                self.alunos = []

