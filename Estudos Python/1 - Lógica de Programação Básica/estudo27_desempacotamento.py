nomes = ['Filipe', 'Tusk', 'Soo']
#nome1, nome2, nome3 = nomes
#nome1, nome2, nome3 = ['Filipe', 'Tusk', 'Soo']

nomes2 = ['TMA', 'MMA']
nomes.extend(nomes2)
print(nomes)

_, _, nome3, *_ = nomes
print(nome3, _)

#tuplas:

outros_nomes = (0, 'Olá')
#outros_nomes.append('Olá2') ERROR, POIS DUPLA É FORMA DA LISTA IMUTAVEL