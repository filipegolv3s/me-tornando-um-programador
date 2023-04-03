valor_total = 0
while True:
    while True:
        escolha_opcao = input('Escolha a opção: \n1 - Iniciar um cálculo novo \n2- Continuar da última soma\n')
        print()
        try:
            escolha_opcao_int = int(escolha_opcao)
            if escolha_opcao_int == 1:
                #primeiro valor que o usuario ira digitar
                number_one = input('Digite o primerio valor: ')
                number_one_int = int(number_one)
                print('Primeiro valor: {}'.format(number_one_int))
                print()

                #operador do calculo:
                operador_escolhido = input('Escolha um operador:\n"+" para adição;\n"-" para subtração;\n"*" para multiplicação;\n"/" para divisão;\n')
                print()
                

                #segundo valor que o usuario ira digitar
                number_two = input('Digite o segundo valor: ')
                number_two_int = int(number_two)
                print('Segundo valor: {}'.format(number_two_int))
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
                
                print('Resultado: {0}'.format(valor_total))
                print()


            if escolha_opcao_int == 2:
                novo_sinal = input('Escolha novamente um operador:\n"+" para adição;\n"-" para subtração;\n"*" para multiplicação;\n"/" para divisão;\n')
                print()

                number_three = input('Digite o novo valor a ser somado:\n')
                number_three_int = int(number_three)
                print()


                #calculando novamente:
                if novo_sinal == '+':
                    valor_continuado = valor_total + number_three_int
                elif novo_sinal == '-':
                    valor_continuado = valor_total - number_three_int
                elif novo_sinal == '*':
                    valor_continuado = valor_total * number_three_int
                elif novo_sinal == '/':
                    valor_continuado = valor_total / number_three_int
                else:
                    print('Ops! Algo deu errado.')
                print(f'{valor_total} {novo_sinal} "=" {valor_continuado} ')
        except:
            print('Perdão! Escreva apenas números: ')
