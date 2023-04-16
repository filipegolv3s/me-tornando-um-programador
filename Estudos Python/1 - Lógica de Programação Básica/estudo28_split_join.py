#strip = corta os espaços do começo e fim
#rstrip = corta só o da direita
#lstrip = corta só o da esquerda
#split = divide uma string
#join = une uma string

frase = '   Olá, eu estou aprendendo python       '
lista_frases = frase.split()
oracoes_da_frase = frase.split(',')
oracoes_da_frase_sem_espaco = []

print(lista_frases)
print(oracoes_da_frase)

for i, oracoes in enumerate(oracoes_da_frase):
    print(oracoes.strip())

for i_e, oracoes_e in enumerate(oracoes_da_frase):
    oracoes_da_frase_sem_espaco.append(oracoes_da_frase[i_e].strip())
print(oracoes_da_frase_sem_espaco)

frases_unida = ', '.join(oracoes_da_frase_sem_espaco)
print(frases_unida)


