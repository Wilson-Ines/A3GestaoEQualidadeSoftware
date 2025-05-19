import unittest
from sistema import SistemaAlunos
from aluno import Aluno
import os

class TestSistemaAlunos(unittest.TestCase):

    def setUp(self):
        # Cria uma instância temporária sem afetar o arquivo real
        self.sistema = SistemaAlunos(arquivo_dados="dados/test_alunos.json")
        self.sistema.alunos = []  # Limpa qualquer dado existente
        self.aluno = Aluno("Teste", 20, "T123")

    def tearDown(self):
        # Remove o arquivo de teste após os testes
        if os.path.exists("dados/test_alunos.json"):
            os.remove("dados/test_alunos.json")

    def test_adicionar_aluno(self):
        self.sistema.adicionar_aluno(self.aluno)
        self.assertEqual(len(self.sistema.alunos), 1)

    def test_adicionar_matricula_duplicada(self):
        self.sistema.adicionar_aluno(self.aluno)
        with self.assertRaises(ValueError):
            self.sistema.adicionar_aluno(Aluno("Outro", 21, "T123"))

    def test_remover_aluno(self):
        self.sistema.adicionar_aluno(self.aluno)
        self.assertTrue(self.sistema.remover_aluno("T123"))
        self.assertEqual(len(self.sistema.alunos), 0)

    def test_buscar_aluno(self):
        self.sistema.adicionar_aluno(self.aluno)
        aluno_encontrado = self.sistema.buscar_aluno("T123")
        self.assertIsNotNone(aluno_encontrado)
        self.assertEqual(aluno_encontrado.nome, "Teste")

    def test_atualizar_aluno(self):
        self.sistema.adicionar_aluno(self.aluno)
        self.sistema.atualizar_aluno("T123", novo_nome="Novo Nome", nova_idade=30)
        aluno_atualizado = self.sistema.buscar_aluno("T123")
        self.assertEqual(aluno_atualizado.nome, "Novo Nome")
        self.assertEqual(aluno_atualizado.idade, 30)
    
    def test_idade_invalida(self):
        with self.assertRaises(ValueError):
            Aluno("Nome", -5, "X001")

if __name__ == "__main__":
    unittest.main()
