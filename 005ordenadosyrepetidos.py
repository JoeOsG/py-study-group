#función
def interseccion(uno, dos):
  final = []
  #recorrido de lista recibida
  for elemento in uno:
    if elemento in dos:
      if elemento not in final:
        final.append(elemento)

  final.sort()      
  print(final)
  
  #Solo separar cada llamada
  print()


interseccion([1, 2, 3, 4, 5, 6, 7, 8], [10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19])
#[1, 6]
interseccion([1, 1, 1], [2, 2, 2])
#[]
interseccion([3, 2, 1], [4, 3, 2, 1])
#[1, 2, 3]
interseccion([1, 2, 3, 4, 5], [0, 2, 4, 6, 8, 10])
#[2, 4]
interseccion([6, 7, 1, 2, 1, 3, 4, 5], [7, 8, 1, 3, 2, 1, 7, 3, 7, 10])
#[1, 2, 3, 7]