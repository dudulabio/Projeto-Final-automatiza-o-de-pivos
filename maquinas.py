class Maquinas:
  def __init__(self,tipo,cultura,velocidade_pivo,linha_pivo,th):
    self.tipo  =  tipo
    self.cultura = cultura
    self.linha_pivo = linha_pivo
    self.th = th
    self.ligado = False

  def ligar(self):
    self.ligado = True
    print(f"{self.tipo} Ligado.")

  def desligar(self):
    self.ligado = False
    print(f"{self.tipo} Desligado.")