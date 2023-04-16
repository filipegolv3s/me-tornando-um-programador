#Criando um valor padrão:

def calculo(x, y, z=None): #Todos os parâmetros, após um parâmetro padrão, devem também ser padronizado.
    if z is None:
        print('Sua equação foi: {0} + {1} = {2}'.format(x, y, x + y))
    else:
        if z == '-':
            print('Sua equação foi: {0} - {1} = {2}'.format(x, y, x - y))
        elif z == '*':
            print('Sua equação foi: {0} * {1} = {2}'.format(x, y, x * y))
        elif z == '/':
            print('Sua equação foi: {0} * {1} = {2}'.format(x, y, x / y))

calculo(10, 23, '*')