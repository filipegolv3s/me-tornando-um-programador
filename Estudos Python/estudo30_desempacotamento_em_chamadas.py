'''
lista = ['Maria', 'Bastos', 1, 2, 3, 4, 'Eduarda', 5, 6, 7]

nome_1, *resto, nome2, _,_,_ = lista
print(nome_1, nome2)

print(*lista)
'''
salas = [
    ['João', 'Aline', 'Jô'],
    
    ['Letícia', 'Thaísa', 'Larissa'],
]

print(*salas, sep='\n')