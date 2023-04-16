nomes = ['Filipe', 'Tusk', 'Soo']

nomes2 = ['TMA', 'MMA']
nomes.extend(nomes2)
print(nomes)

lista_enumerada = enumerate(nomes)
print(lista_enumerada)
print(next(lista_enumerada), next(lista_enumerada), next(lista_enumerada))
print(next(lista_enumerada), next(lista_enumerada))

for item in lista_enumerada:
    print(item)
print('O que tem na {l_e}'.format(l_e = lista_enumerada))
#ELE NÃO RETORNA NADA, POIS ELE JÁ FOI USADO.

nova_lista_enumerada = list(enumerate(nomes, start=1))
print(nova_lista_enumerada)
for item_de_cada_x in nova_lista_enumerada:
    print(item_de_cada_x)