 
from Assinante import Assinante
class PlataformaStreaming:
    def __init__(self):
        self.assinantes = []
    
   

    def cadastro(self):
        plano = {
             "1": "Basico",
             "2": "Padrão",
             "3": "Premium"
        }


        nome = input("Informe o nome do assinante: ")

        print("Selecione o plano: [1] Basico | [2] Padrão | [3] Premium")

        plano_selecionado = input(">")

        senha = input("Informe sua senha: ")

        novo_assinante = Assinante(nome, plano[plano_selecionado], senha)
        self.assinantes.append(novo_assinante)

    def listar_assinantes(self):

        if not self.assinantes:
            print("Nenhum assinante cadastrado.")
            return
        
        for assinante in self.assinantes:
            print(assinante.exibir_dados())


    def buscar_por_id(self, id_conta):
        for assinante in self.assinantes:
            if assinante.id_conta == id_conta:
                return assinante

        return None


    def cancelar_assinatura(self, id_conta):
        assinante = self.buscar_por_id(id_conta)

        if assinante:
            self.assinantes.remove(assinante)
            return True


        return False

     
             









plataforma = PlataformaStreaming()


     
    
        