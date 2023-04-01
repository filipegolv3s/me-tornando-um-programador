"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''
try:
    valor_digitado = input('Digite um número inteiro: ')
    valor_digitado_int = int(valor_digitado)
    par_impar = valor_digitado_int % 2 == 0
    if par_impar == True:
        print('\'{}\' é par'.format(valor_digitado_int))
    elif par_impar == False:
        print('\'{}\' é ímpar'.format(valor_digitado_int))
except:
    print('\'{}\'não é um valor inteiro'.format(valor_digitado))
'''


#CORREÇÃO DO PROFESSOR:

#entrada = input('Digite um número: ')
# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


#APRENDIZADO OBSERVANDO O DO PROFESSOR
# 1- ele utilizou o isdigit
# 2- ele definiu uma variavel com um valor 'impar' \
# e utilizou o if para re-atribuir o valor 'par'


#Reescrevendo meu codigo com as lições acima:

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_digitado = input('Digite um número inteiro: ')

if num_digitado.isdigit():
    num_int_digitado = int(num_digitado)
    conferir_valor = num_int_digitado % 2 == 0
    par_impar = 'ímpar'
    # DESTA MANEIRA, O NÚMERO SEMPRE IMPAR, A NAO SER QUE RE-ATRIBUIAMOS

    if conferir_valor:
        par_impar = 'par'

    print('\'{v1}\' é {v2}'.format(v1 = num_int_digitado, v2 = par_impar))
else:
    print('Desculpe! Você não digitou um número inteiro.')