import re

def revisar(secuencia):
    dividido = re.findall('...',secuencia)
    
    primero = 1
    contador = 0
    for sec in dividido:
      if primero == 1:
        if sec == 'AUG':
          primero = 0
      else :
        if sec == 'UAA':
          contador += 1
          primero = 1
        if sec == 'UAG':
          contador += 1
          primero = 1
        if sec == 'UGA':
          contador += 1
          primero = 1

    print("Secuencias detectadas: " + str(contador))
          
    # print(dividido)
    # print(secuencia)

revisar('AUGGGGUACUACUAUAGGUAG')
revisar('AUGGGGUaUxAXUA-AGGUaG')
revisar('AUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAG')

