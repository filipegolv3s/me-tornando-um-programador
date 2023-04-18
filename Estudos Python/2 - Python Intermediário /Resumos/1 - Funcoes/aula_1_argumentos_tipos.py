# 1 - Argumentos posiçonais:

def soma(x, y):
    print('A soma de {0} + {1} = {2}'.format(x, y , x + y))

soma(135, 123) # Vão pela posição dos argumentos em relação aos parâmetros

# 2 - Argumentos nomeados:

soma(y=135, x=123) # Vão pelos argumentos que passamos para cada parâmetros
#----------------------------

# 3 - Após nomearmos um parâmetros, todos os seguintes devem ser nomeados:

#Errado: soma(y=123, 4)

#Certo: soma(y=123, x=4)