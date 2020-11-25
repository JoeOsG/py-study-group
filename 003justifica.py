def justifica(trabajo):
#  treinta = []
#  treinta[:0] = trabajo
  if len(trabajo) < 29:
    contador = len(trabajo)
    
    while contador < 30:
#      print('e')
      trabajo = trabajo + ' '
      contador+=1
#    
    trabajo = trabajo + '\n'

  print(trabajo[0:30])


justifica('Hola5678911234567892123456789314')
justifica('Hola')