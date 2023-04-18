x = 25 #1

def funcao(): #3
    x = 12
    print('Este é o x da função: {0}'.format(x))

funcao()  #2 
print('Este é o x global: {0}'.format(x)) #4


#---------------------------------------
def funcao_2(x): # 6 neste caso, vamos chamar o x, porque ele foi o argumento na funcao_2
    print(x)
    x = 12
    print('Este é o x da função mudada: {0}'.format(x))


funcao_2(x) # 5

print('Este é o x global 2: {0}'.format(x)) # X continua sendo 25, mesmo após tudo #final
