#Questão 01
class Televisao:
    def __init__(self, canal, estaLigada):
        self.canal = 0
        self.estaLigada = False

    def mudar_canal_cima(self):
        self.canal=self.canal+1
    
    def mudar_canal_baixo(self):
        self.canal=self.canal-1

    def exibir_informacoes(self):
        print(f"Canal: {self.canal}")
        print(f"Status: {self.estaLigada}")
            