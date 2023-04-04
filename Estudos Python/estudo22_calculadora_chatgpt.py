# Bom, pedir ao chat gpt que limpaze e deixasse mais legível meu código, isso para que eu pudesse analisar um código mais limpo de um programa que eu fiz. Estou feliz com meu código, mas achei incrível.

import os

valor_total = 0
continuacao = False

while True:
    # exibir as opções ao usuário
    print('Escolha a opção:')
    print('1 - Iniciar um cálculo novo')
    print('2 - Continuar do último cálculo')
    print('3 - Para limpar o programa')
    print('4 - Para sair do programa')
    escolha_opcao = input()

    try:
        escolha_opcao_int = int(escolha_opcao)

        if escolha_opcao_int == 4:
            # sair do loop
            break
        elif escolha_opcao_int == 3:
            # limpar a tela
            os.system('cls' if os.name == 'nt' else 'clear')
        elif escolha_opcao_int == 1:
            # solicitar primeiro número
            os.system('cls' if os.name == 'nt' else 'clear')
            number_one = int(input('Digite o primeiro valor: '))
            
            # solicitar o operador
            operadores = {'+': 'adição', '-': 'subtração', '*': 'multiplicação', '/': 'divisão'}
            operador_escolhido = input(f'Escolha um operador: {", ".join(operadores.keys())}\n')
            if operador_escolhido not in operadores:
                raise ValueError('Operador inválido.')
            
            # solicitar segundo número
            number_two = int(input('Digite o segundo valor: '))
            
            # realizar o cálculo
            if operador_escolhido == '+':
                valor_total = number_one + number_two
            elif operador_escolhido == '-':
                valor_total = number_one - number_two
            elif operador_escolhido == '*':
                valor_total = number_one * number_two
            elif operador_escolhido == '/':
                valor_total = number_one / number_two
            
            # exibir resultado
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Resultado da {operadores[operador_escolhido]}: {valor_total}')
            continuacao = True
            
        elif escolha_opcao_int == 2:
            # verificar se há um cálculo anterior
            if continuacao:
                # solicitar o operador
                operadores = {'+': 'adição', '-': 'subtração', '*': 'multiplicação', '/': 'divisão'}
                operador_escolhido = input(f'Escolha um operador: {", ".join(operadores.keys())}\n')
                if operador_escolhido not in operadores:
                    raise ValueError('Operador inválido.')
                
                # solicitar o próximo número
                number_three = int(input('Digite o novo valor a ser calculado:\n'))
                
                # realizar o novo cálculo
                if operador_escolhido == '+':
                    valor_total = valor_total + number_three
                elif operador_escolhido == '-':
                    valor_total = valor_total - number_three
                elif operador_escolhido == '*':
                    valor_total = valor_total * number_three
                elif operador_escolhido == '/':
                    valor_total = valor_total / number_three
                
                # exibir resultados
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Resultado da {operadores[operador_escolhido]}: {valor_total}')
                continuacao = True
            else:
                print('Não há cálculo anterior para continuar.')
        else:
            print('Opção inválida.')
    except ValueError:
        print('Digite uma opção válida.') 
