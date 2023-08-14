import numpy as np
class Ponto:  #definicao da classe

  def __init__(self, x: float, y: float):  #passagem de parametros da classe
    self.x = x  #atribuindo valores
    self.y = y  #atribuindo valores

  '''ja libera automaticamente'''

  def imprime(self):  #definindo função que imprime
    print(f"o valor de x é: {self.x} e o valor de y é {self.y}")

  def distancia(self, x2, y2):
    
    return np.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
