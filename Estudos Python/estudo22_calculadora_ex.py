import os

valor_total = 0
continuacao = False
while True:
    escolha_opcao = input('Escolha a opção: \n1 - Iniciar um cálculo novo \n2 - Continuar do último cálculo\n3 - Para limpar o programa\n4 - Para sair do programa\n')
    print()
    try:
        escolha_opcao_int = int(escolha_opcao)
        if escolha_opcao_int == 4:
            break
        if escolha_opcao_int == 3:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        if escolha_opcao_int == 1:
            #primeiro valor que o usuario ira digitar
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            number_one = input('Digite o primerio valor: ')
            number_one_int = int(number_one)
            print()

            #operador do calculo:
            operador_escolhido = input('Escolha um operador:\n"+" para adição;\n"-" para subtração;\n"*" para multiplicação;\n"/" para divisão;\n')
            print()
            

            #segundo valor que o usuario ira digitar
            number_two = input('Digite o segundo valor: ')
            number_two_int = int(number_two)
            print()

            #calculando:
            if operador_escolhido == '+':
                valor_total = number_one_int + number_two_int
            elif operador_escolhido == '-':
                valor_total = number_one_int - number_two_int
            elif operador_escolhido == '*':
                valor_total = number_one_int * number_two_int
            elif operador_escolhido == '/':
                valor_total = number_one_int / number_two_int
            else:
                print('Ops! Algo deu errado.')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print('Resultado: {0}'.format(valor_total))
            print()
            continuacao = True


        if escolha_opcao_int == 2 and continuacao == True:
            operador_escolhido = input('Escolha novamente um operador:\n"+" para adição;\n"-" para subtração;\n"*" para multiplicação;\n"/" para divisão;\n')
            print()

            number_three = input('Digite o novo valor a ser calculado:\n')
            number_three_int = int(number_three)
            print()


            #calculando novamente:
            if operador_escolhido == '+':
                valor_total = valor_total + number_three_int
            elif operador_escolhido == '-':
                valor_total = valor_total - number_three_int
            elif operador_escolhido == '*':
                valor_total = valor_total * number_three_int
            elif operador_escolhido == '/':
                valor_total = valor_total / number_three_int
            else:
                print('Ops! Algo deu errado.')
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            print('Resultado: {0}'.format(valor_total))
            print()
        elif escolha_opcao_int == 2 and continuacao == False:
            print('Você ainda não somou nada')
            print()
    except:
        print('Perdão! Escreva apenas números: ')