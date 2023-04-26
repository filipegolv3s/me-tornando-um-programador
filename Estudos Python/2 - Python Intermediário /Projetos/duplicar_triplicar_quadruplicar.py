import os

def texto_destacado(opcao):
    linhas = '-' * 30
    return ('{0}\n{1}\n{0}'.format(linhas, opcao))

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar
    
duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

while True:
    opcao_escolhida = input('Escolha o que você deseja:\n1 - Sair do programa;\n2 - Duplicar;\n3 - Triplicar;\n4 - Quadruplicar;\n')
    if opcao_escolhida == '1':
        break
    elif opcao_escolhida == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('DUPLICAR'))
        duplicar_number = input('2 x ')
        if not duplicar_number.isdigit():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(texto_destacado('Digite apenas números!'))
            continue
        duplicar_number = int(duplicar_number)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('2 x {0} = {1}'.format(duplicar_number, duplicar(duplicar_number))))

    elif opcao_escolhida == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('TRIPLICAR'))
        triplicar_number = input('3 x ')
        if not triplicar_number.isdigit():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(texto_destacado('Digite apenas números!'))
            continue
        triplicar_number = int(triplicar_number)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('3 x {0} = {1}'.format(triplicar_number, triplicar(triplicar_number))))

    elif opcao_escolhida == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('QUADRUPLICAR'))
        quadruplicar_number = input('4 x ')
        if not quadruplicar_number.isdigit():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(texto_destacado('Digite apenas números!'))
            continue
        quadruplicar_number = int(quadruplicar_number)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('4 x {0} = {1}'.format(quadruplicar_number, quadruplicar(quadruplicar_number))))
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(texto_destacado('Escolha uma opção válida!'))
        continue

