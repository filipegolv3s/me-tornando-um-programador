"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
'''
texto = 'Filipe'.__iter__() # iter('FIlipe)
primeira_letra = texto.__next__() 
segunda_letra = texto.__next__()
print(primeira_letra)
print(segunda_letra)
'''



# for letra in texto
texto = 'Luiz'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)print(texto)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)