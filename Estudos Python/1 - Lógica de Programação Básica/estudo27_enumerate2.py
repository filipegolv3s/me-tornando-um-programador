nomes = ['Filipe', 'Tusk', 'Soo']

nomes2 = ['TMA', 'MMA']
nomes.extend(nomes2)

'''
nova_lista_enumerada = list(enumerate(nomes, start=1))
#print(nova_lista_enumerada)

for item_de_cada_x in nova_lista_enumerada:
    print(item_de_cada_x)
'''

# O enumerate automaticamente cria uma tupla, sendo isso verdade, podemos desempacotar de forma prática, direto no for


for a, b in enumerate(nomes, start=1):
    print(a, b)
