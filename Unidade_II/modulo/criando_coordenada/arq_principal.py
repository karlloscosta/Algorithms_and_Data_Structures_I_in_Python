#import ponto
from ponto import Ponto #dentro do arquivo ponto importe Ponto
if __name__ == '__main__': #arquivo principal
  x = input('digite a coordenada x')
  y = input('digite a coordenada y')
  p = Ponto(x,y)
  p.imprime()
