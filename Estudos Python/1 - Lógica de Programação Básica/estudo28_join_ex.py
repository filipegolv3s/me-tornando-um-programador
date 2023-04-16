nome = 'Filipe Golves'
qtd_letras = len(nome)
nome_separado = []
quero_ver = range(qtd_letras)

for i in range(qtd_letras):
    nome_separado += nome[i]
nome_modificado = '*'.join(nome_separado)

print(nome_modificado)
