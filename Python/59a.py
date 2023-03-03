palavra_inicial = input()

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
maiusculas_contador = 0
minusculas_contador = 0

for letra in palavra_inicial:
    if letra in maiusculas:
        maiusculas_contador += 1
    else:
        minusculas_contador += 1

if maiusculas_contador > minusculas_contador:
    print(palavra_inicial.upper())
else:
    print(palavra_inicial.lower())


