#    https://www.programiz.com/python-programming/online-compiler/


    import re

def revisar(secuencia):
    dividido = re.findall('...',secuencia)
    print(dividido)
    print(secuencia)

revisar('AUGGGGUACUACUAUAGGUAG')
revisar('AUGGGGUaUxAXUA-AGGUaG')
revisar('AUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAGAUGGGGUAUUAUUAUAGGUAG')


#['12', '34', '56', '78', '90']