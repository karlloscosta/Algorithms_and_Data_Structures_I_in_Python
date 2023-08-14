if __name__ == '__main__':  #arquivo principal
  x = 4
  y = 3

  p = Ponto(float(x) , float(y))
  p.imprime()
  distancia_pontos = p.distancia(3, 3)
  print(distancia_pontos)
