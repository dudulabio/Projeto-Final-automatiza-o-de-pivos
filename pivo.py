from maquinas import Maquinas

class Pivo(Maquinas):

    def __init__(self,tipo,cultura, velocidade_pivo,linha_pivo,th):
       super().__init__(tipo,cultura,velocidade_pivo,linha_pivo,th)
       self.velocidade_pivo = velocidade_pivo


    def imprimir(self):
            print(f"Tipo: {self.tipo}")
            print(f'Talhão: {self.th}')
            print(f'Cultura: {self.cultura}')
            print(f'Velocidade do pivo em metros/hr: {self.velocidade_pivo}')
            print(f'Alcance da linha do pivo em metros: {self.linha_pivo}')

    def irrigar(self):
        if self.ligado:
                print(f"{self.tipo} {self.cultura} irrigando.")
        
    def desligar_pivo(self):
            self.desligar()

