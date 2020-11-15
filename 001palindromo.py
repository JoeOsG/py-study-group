def espalindromo(frase):
    espalindromo = 1
    contador = 1
    for letra in frase:
        if letra.lower() != frase[contador*-1].lower():
            espalindromo = 0
        
        contador+=1
    
    if espalindromo == 0:
        print ("«" + frase + "» no es un palíndromo")
    else:
        print ("ÉXITO la frase «" + frase + "» es un palíndromo")



espalindromo('Anitalavalatina')
espalindromo('xAnitalavalatina')