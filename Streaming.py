
from Assinante import Assinante
class PlataformaStreaming:
    assinantes = []

    def cadastrar(self):
        plano = {
             "1"|"Basico",
             "2"|"Padrão"
             "3"|"Premium"
        }

        nome = input("Informe o nome do assinante: ")
        print("Selecione o plano: [1] Basico | [2] Padrão | [3] Premium")
        plano_selecionado = input(">")
        senha = input("Informe sua senha: ")
        