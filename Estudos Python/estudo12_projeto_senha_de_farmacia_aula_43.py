# Operador 'And', 'Or' e 'Not' - Aula 40 - 43
comando_entrada = input('[E]ntrar e [S]air: ')

senha_criada = 'drogariapc40'

if (comando_entrada == 'E' or comando_entrada == 'e'):
    senha_de_acesso = input('Crie sua senha com \'.\': ')
    if ('.' in senha_de_acesso) and (senha_criada == 'drogariapc40'):
        print('Acesso permitido')
    else:
        print('Acesso negado')
