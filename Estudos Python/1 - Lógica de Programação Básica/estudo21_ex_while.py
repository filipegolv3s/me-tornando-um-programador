nome = input('Digite seu nome: ')
qtd_letras = len(nome)
como_ficara = ''
reescrevendo_nome = 0

while reescrevendo_nome < qtd_letras:
    como_ficara += '*' + nome[reescrevendo_nome]
    reescrevendo_nome += 1

print(como_ficara)
'''
#correcao:
nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
'''