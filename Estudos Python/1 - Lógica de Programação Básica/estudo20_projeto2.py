
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    horario_usr = input('Digite que horas são: ')
    horario_usr_int = int(horario_usr)
    if horario_usr_int >= 0 and horario_usr_int <= 11:
        print('Bom dia!')
    elif horario_usr_int >= 12 and horario_usr_int <= 17:
        print('Boa tarde!')
    elif horario_usr_int >= 18 and horario_usr_int <= 23:
        print('Boa noite!')
except:
    print('Perdão! Horario digitado inválido! ')

#CORREÇÃO DO PROFESSOR

"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""


# DESTA VEZ, ACHEI CURIOSO QUE MEU CODIGO FICOU PRATICAMENTE IGUAL AO DO PROFESSOR, APESAR DE NAO TER USADO O ELSE PARA CASO NAO TENHA UMA HORA CERTA