"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usr = input('Digite seu nome: ')

nome_curto = len(nome_usr) <= 4
nome_normal = len(nome_usr) == 5 and len(nome_usr) == 6
#ANTES ERA 'OR', ERRO MEU

nome_grande = len(nome_usr) > 6
if nome_curto:
    print('Seu nome é curto.')
elif nome_normal:
    print('Seu nome é normal.')
elif nome_grande:
    print('Seu nome é muito grande.')
else:
    print('Erro inesperado. Entre em contato com ...')


"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
"""

#AO MEU VER, MEU CODIGO ESTÁ DE CERTA FORMA, BOM, MAS FALTOU PONTOS QUE O PROFESSOR PONTUOU QUE FAZ TOTAL DIFERENÇA. COM EXCEÇÃO DO NOME_NORMAL QUE ERA PRA TER SIDO O 'AND' AO INVES DO 'OR'