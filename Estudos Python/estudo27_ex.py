import os

lista_de_compras = []
while True:
    escolha_do_usr = input('Selecione uma opção:\n[i]nserir, [a]pagar, [l]istar:')
    if escolha_do_usr == 'i':
        if os.name == 'nt':
            os.system('cls')
        else: 
            os.system('clear')
        print('Sua lista de compras: {}'.format(lista_de_compras))
        opcao_isr = input('Digite o item que você precisa comprar: ')
        lista_de_compras.append(opcao_isr)
        print(lista_de_compras)
    else:
        print('Opção ainda não construida')