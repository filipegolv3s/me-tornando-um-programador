#Parametro são as cada váriaveis que serão definadas, no caso abaixo: 'a, b, c'
def Python(a, b, c):
    print(a)
    print(c)
    print(b)

Python(123, 'Filipe', 'Arroz') #E aqui são argumentos, valores que definimos nas variaveis


#------------------------------------------------------------------------
#  Ex.:
def falar_nome(nome = 'Sem nome'):

    print(
        'Olá, {}! Seja bem-vindo!'.format(nome)
)

falar_nome('Filipe')
falar_nome()

#------------------------------------------------------------------------
#  Ex.:

def some(num1, num2):
    soma = num1 + num2
    print('A sua equação foi: {0} + {1} = {2}'.format(num1, num2, soma))


some(25, 123)
#------------------------------------------------------------------------