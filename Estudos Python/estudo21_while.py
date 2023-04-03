#aula1
'''
while True:
    numb = input('Digite um número: ')

    if numb == 'sair':
        break
'''
'''
#aula 2
contador = 0
while contador <= 10:
    print(contador)
    contador += 1

print('Acabou!')
'''
#aula 3
#  = += -= *= /= //= **= %=

#aula 4
'''
contador = 0
while contador <= 100:
    contador += 1

    if contador >= 45 and contador <= 77:
        print(f'Não vou mostrar {contador}')
        continue

    print(contador)

    if contador == 86:
        print(contador)
        break

print('Acabou!')
'''

#download:
updownload_total = 10
updownload_parcial = 10

total_baixado = 0
while total_baixado <= updownload_total:
    parcial_baixado = 0
    while parcial_baixado <= updownload_parcial:
        print('Total baixado: {0}0% mb Parcial baixado:{1}0% mb'.format(total_baixado, parcial_baixado, 0))
        parcial_baixado += 1
    total_baixado += 1