import os
import time

NUMERO_MAXIMO_OPCOES = 8
NUMERO_PERGUNTAS = 3

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def letragavalor(letra):
    letra = letra.lower()
    return ord(letra) - ord('a')

def imprimir_opcoes(opcoes):
    for i, opcao in enumerate(opcoes):
        letra = chr(ord('A') + i)
        print(f'{letra}) {opcao}')

def mensagem(texto):
    linha = '-' * 30
    return f'{linha}\n{texto}\n{linha}'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def apenas_uma_letra(mensagem):
    while True:
        escolha = input(mensagem)
        if len(escolha) == 1:
            return escolha
        else:
            print('Digite apenas uma letra')
            time.sleep(2)

acertos = 0

for pergunta in perguntas:
    while True:
        limpar_tela()
        print(f'Pergunta: {pergunta["Pergunta"]}\n')
        print('Opções:')
        imprimir_opcoes(pergunta['Opções'])

        escolha_do_usr = apenas_uma_letra('Escolha uma opção: ')
        opcao_escolhida = letragavalor(escolha_do_usr)
        
        if opcao_escolhida < len(pergunta['Opções']):
            if pergunta['Opções'][opcao_escolhida] == pergunta['Resposta']:
                print()
                print(mensagem('Você acertou ✅'))
                acertos += 1
            else:
                print(mensagem('Você errou ❌!'))
            time.sleep(2)
            break
        else:
            print(mensagem('Escolha uma opção válida!'))
            time.sleep(2)
            continue

if acertos == 0:
    limpar_tela()
    print(mensagem('Poxa! Você não acertou nenhuma 😕. Continue tentando!🙂'))
elif acertos == 1:
    limpar_tela()
    print(mensagem('Parabéns! Você acertou 1/3 😀. Continue melhorando!🙂'))
elif acertos == 2:
    limpar_tela()
    print(mensagem('Parabéns! Você acertou 2/3 😀. Continue melhorando!🙂'))
elif acertos == 3:
    limpar_tela()
    print(mensagem('Uau! Você acertou TODAS 😁!'))
