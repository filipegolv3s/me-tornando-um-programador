nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and int(idade):
  print('Seu nome é: {nome} \nSeu nome invertido é: {nome_invertido}'.format(nome = nome, nome_invertido = nome[::-1]))
  if (' ' in nome) == True:
    print('Seu nome tem espaços? Sim')
  elif (' ' in nome) == False:
    print('Seu nome tem espaços? Não')
  print('Seu nome tem \'{q_letras}\' letras \nA primeira letra é: \'{primeira_letra}\' \nA última letra do seu nome é: \'{ultima_letra}\' '.format(q_letras = len(nome), primeira_letra = nome[0], ultima_letra = nome[-1]))
else:
  print('Desculpe, você deixou campos vazios.')
    
  

'''

else:
  print('nada')
'''
