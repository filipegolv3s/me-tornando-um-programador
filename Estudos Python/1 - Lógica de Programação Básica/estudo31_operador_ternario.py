'''
senha = input('Digite sua senha:')

condicao = 'Senha criada' if len(senha) <= 5 else 'Digite uma senha menor que 5'
print(condicao)
'''
condicao_1 = False
condicao_2 = True
print('Primeiro valor' if condicao_1 else 'Segundo valor' if condicao_2 else 'Terceiro valor')