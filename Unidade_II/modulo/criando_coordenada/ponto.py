class Ponto:  #definicao da classe

  def __init__(self, x: float, y: float):  #passagem de parametros da classe
    self.x = x  #atribuindo valores
    self.y = y  #atribuindo valores

  '''ja libera memoria automaticamente'''

  def imprime(self):#definindo função que imprime
    print(f"o valor de x é: {self.x} e o valor de y é {self.y}")
