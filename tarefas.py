# tarefas.py

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✔️" if self.concluida else "❌"
        return f"{status} {self.titulo}: {self.descricao}"


# Lista global de tarefas
tarefas = []


# ✅ Criar tarefa
def criar_tarefa(titulo, descricao):
    nova = Tarefa(titulo, descricao)
    tarefas.append(nova)
    return nova


# 📋 Listar tarefas
def listar_tarefas():
    return tarefas


# ✏️ Atualizar tarefa
def atualizar_tarefa(indice, novo_titulo=None, nova_descricao=None):
    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice]
        if novo_titulo:
            tarefa.titulo = novo_titulo
        if nova_descricao:
            tarefa.descricao = nova_descricao
        return tarefa
    return None


# ❌ Excluir tarefa
def excluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        return tarefas.pop(indice)
    return None


# ✔️ Concluir tarefa
def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice].concluir()
        return tarefas[indice]
    return None