frase = 'O Python é uma linguagem de programção multiparadigma. Python foi criado por Guido van Rossum.'
frase = frase.lower()

# count mostra quantas vezes uma palavra, sílaba aparece.
#print(frase.count('python'))

apareceu_mais_x = 0
letra_mais_x = ''
i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if quantas_vezes_letra_apareceu > apareceu_mais_x:
        apareceu_mais_x = quantas_vezes_letra_apareceu
        letra_mais_x = letra_atual

    print(letra_atual)
    i += 1

print(letra_mais_x)