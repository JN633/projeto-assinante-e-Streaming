import random
import hashlib



class Assinante:
    def __init__(self, nome, plano, senha):
        self.id_conta = random.randint(1000, 9999)
        self.nome = nome
        self.plano = plano
        self.senha_hash = self._gerar_hash(senha)

    def __str__(self):
        return f"ID: {self.id_conta}\nNome: {self.nome}\nPlano: {self.plano}"

    def _gerar_hash(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def exibir_dados(self):
        return f"Seu Id: {self.id_conta}\nSeu Nome: {self.nome}\nSeu Plano: {self.plano}\nSua Senha: {self.senha_hash}"

    