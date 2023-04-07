'''
lista = ['Maria', 'Helena', 'Luiz', 'FIlipe']
i = 0
for nomes in lista:
    print('Indice: {idc} e Valor: {vlr}'.format(idc = i, vlr = lista[i]))
    i += 1
'''
# CODIGO FUNCIONANDO PERFEITAMENTE, POREM, EU DEVERIA TER USADO RANGE AO INVES DO MANUAL "I += 1"
# OU SEJA:

lista = ['Maria', 'Helena', 'Luiz', 'FIlipe', 12]
i = range(len(lista))
for indices_separado in i:
    print('Indice: {idc} e Valor: {vlr}'.format(idc = indices_separado, vlr = lista[indices_separado]))


#CORREÇÃO DO PROFESSOR:
'''
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
'''