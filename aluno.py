class Aluno:
    def __init__(self, nome, idade, matricula):
        # Vamos definir que o aluno tem que ter nome, matrícula e idade maior que 0
        if not nome or not matricula or idade <= 0:
            raise ValueError("Os dados inseridos estão incorretos para o aluno")
        
        # Definimos 3 atributos abaixo
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    # Transforma o "Aluno" em um dicionário Python para salvar no arquivo Json
    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "matricula": self.matricula}
    
    # Formato em String
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}"