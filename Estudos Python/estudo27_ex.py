import os

lista_de_compras = []
while True:

    #Opção para o usuário escolher:
    escolha_do_usr = input('Selecione uma opção:\n[i]nserir, [a]pagar, [l]istar:')

# ---------------------------------------------------------------------------------------

    #I - Opção Adicionar:
    if (escolha_do_usr == 'i') or (escolha_do_usr == 'I'):

        #1 - Limpar tela:
        if os.name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')

        #2 - Adicionar:
        opcao_isr = input('Digite o item que você precisa comprar: ')

        #3 - Evitando espaços vazios:
        if (opcao_isr == '') or (opcao_isr == ' '):
            if os.name == 'nt': 
                os.system('cls')
            else: 
                os.system('clear')
            continue
        else:
            lista_de_compras.append(opcao_isr)

        #4 - Limpar a tela para começar de novo
        if os.name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')

# ---------------------------------------------------------------------------------------

    #II - Opção apagar:
    elif (escolha_do_usr == 'a') or (escolha_do_usr == 'A'):
        if lista_de_compras:

            #1 - Índice a apagar:
            opcao_apg = input('Digite o índice para apagar: ')

            #2 - Verificar se é um número.
            if opcao_apg.isdigit():

                #2.1.1 - Se tudo acontecer corretamente, execute a função apagar:
                try:
                    opcao_apg_int = int(opcao_apg)
                    lista_de_compras.pop(opcao_apg_int - 1)

                    #2.1.2 - Limpar tela para a próxima opção:
                    if os.name == 'nt': 
                        os.system('cls')
                    else: 
                        os.system('clear')

                #2.2.1 - Caso o número seja maior do que o que tem na lista: 
                except:
                    if os.name == 'nt': 
                        os.system('cls')
                    else: 
                        os.system('clear')
                        #2.2.2 - Mensagem 
                        print('Você digitou um índice maior do que os itens que tem na sua lista.')
                        print()

            else:

                #2.3.1 - Se não for um número:
                if os.name == 'nt': 
                    os.system('cls')
                else: 
                    os.system('clear')

                #2.3.2 - Mensagem:
                print('Você não digitou um índice. Digite apenas números!')
                print()
        #Caso não tenha item
        else:
            if os.name == 'nt': 
                os.system('cls')
            else: 
                os.system('clear')
            print('Você ainda não tem item na sua lista.')
            print()

# ---------------------------------------------------------------------------------------


    #III - Opção listar:
    elif (escolha_do_usr == 'l') or (escolha_do_usr == 'L'):

        #1 - Limpar tela:
        if os.name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')

        #2 - Listar:
        if lista_de_compras:
            print('Sua lista de compras:')
            for numeros, itens in enumerate(lista_de_compras, start=1):
                print(numeros, '-', itens)
        #3 - Caso não tenha nada pra listar
        else:
            print('Sua lista está vazia.')
        print()       

# ---------------------------------------------------------------------------------------

    #Caso tenha um opção ínvalida:
    else:
        if os.name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')

        print('Digite uma opção válida!')
        print()