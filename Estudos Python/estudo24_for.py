#while serve para quando não sabemos quantas repetições irão existir

'''
familia = ['Filipe', 'Tusk']
for nomes in familia:
    print(nomes)
'''

nome_digitado = input('Digite seu nome e sobrenome: ')
caracter_escolhido = input('Escolha um caracter: ')
nome_modificado = ''
for silaba in nome_digitado:
    silabamudada = silaba + caracter_escolhido
    nome_modificado = nome_modificado + silabamudada
print(f'{caracter_escolhido}' + nome_modificado)