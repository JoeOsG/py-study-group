#función
def print_numeros(data):
  #recorrido de lista recibida
  for elemento in data:
    print(elemento)
  
  #Solo separar cada llamada
  print()


print_numeros([1, 2, 3, 4, 5])
#1
#2
#3
#4
#5
print_numeros([1, 1, 1])
#1
#1
#1
print_numeros([3, 2, 1])
#3
#2
#1
print_numeros([10, 20, 30, 14, 14, 16, 20])