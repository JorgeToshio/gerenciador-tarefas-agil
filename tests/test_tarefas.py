import unittest
from tarefas import (
    criar_tarefa,
    listar_tarefas,
    atualizar_tarefa,
    excluir_tarefa,
    concluir_tarefa,
    tarefas  # acessa a lista diretamente para limpar entre testes
)

class TestTarefas(unittest.TestCase):

    def setUp(self):
        tarefas.clear()  # limpa a lista antes de cada teste

    def test_criar_tarefa(self):
        t = criar_tarefa("Testar", "Ver se funciona")
        self.assertEqual(t.titulo, "Testar")
        self.assertFalse(t.concluida)
        self.assertEqual(len(tarefas), 1)

    def test_listar_tarefas(self):
        criar_tarefa("A", "Desc A")
        criar_tarefa("B", "Desc B")
        lista = listar_tarefas()
        self.assertEqual(len(lista), 2)

    def test_atualizar_tarefa(self):
        criar_tarefa("Original", "Texto")
        atualizar_tarefa(0, novo_titulo="Novo", nova_descricao="Atualizado")
        t = tarefas[0]
        self.assertEqual(t.titulo, "Novo")
        self.assertEqual(t.descricao, "Atualizado")

    def test_concluir_tarefa(self):
        criar_tarefa("Finalizar", "Teste")
        concluir_tarefa(0)
        self.assertTrue(tarefas[0].concluida)

    def test_excluir_tarefa(self):
        criar_tarefa("Excluir", "Teste")
        excluir_tarefa(0)
        self.assertEqual(len(tarefas), 0)

if __name__ == '__main__':
    unittest.main()