import random
import hashlib

assinante = []

class Assinante:
    def __init__(self, id = "", nome = "" , plano = "", senha = ""):
        self.id = id = random.randint(1000, 9999)
        self.nome = nome
        self.plano = plano
        self.senha_hash = self._gerar_hash(senha)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nPlano: {self.plano}"

    def _gerar_hash(senha):
        return hashlib.sha256(senha.encode()).hexdigest

    def exibir_dados(self):
        return f"Seu Id: {self.id}\nSeu Nome: {self.nome}\nSeu Plano: {self.plano}\nSua Senha: {self.senha_hash}"

    