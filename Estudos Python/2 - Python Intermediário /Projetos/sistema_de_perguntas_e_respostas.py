import os
import time

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

def criarletrasparavalores(numero):
    if numero == 0:
        return 'A'
    elif numero == 1:
        return 'B'
    elif numero == 2:
        return 'C'
    elif numero == 3:
        return 'D'
    elif numero == 4:
        return 'E'
    elif numero == 5:
        return 'F'
    elif numero == 6:
        return 'G'
    elif numero == 7:
        return 'H'

def letrageravalor(letra):
    letra = letra.lower()
    if letra == 'a':
        return 0
    elif letra == 'b':
        return 1
    elif letra == 'c':
        return 2
    elif letra == 'd':
        return 3
    elif letra == 'e':
        return 4
    elif letra == 'f':
        return 5
    elif letra == 'g':
        return 6
    elif letra == 'h':
        return 7

        


def mensagem(texto):
    return ('{linhas}\n{t}\n{linhas}'.format(t = texto,linhas = '-' * 30))
        
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
        print('Pergunta: {0}\n'.format(pergunta.get('Pergunta')))
        print('Opções:')
        contandor = 0
        for options in pergunta.get('Opções'):
            print('{0}) {1}'.format(criarletrasparavalores(contandor),options))
            contandor += 1

        try:
            escolha_do_usr = input('Escolha uma opção: ')
            opcaoescolhida = letrageravalor(escolha_do_usr)
        
            if opcaoescolhida <= len(pergunta['Opções']):
                if pergunta['Opções'][opcaoescolhida] == pergunta['Resposta']:
                    print()
                    print(mensagem('Você acertou ✅'))
                    acertos += 1
                else:
                    print()
                    print(mensagem('Você errou ❌!'))
                time.sleep(2)
                break
            else:
                print()
                print(mensagem('Escolha uma opção válida!'))
                time.sleep(2)
                continue
        except:
            print()
            print(mensagem('Escolha uma opção válida!'))
            time.sleep(2)
            continue

if acertos == 0:
    limpar_tela()
    print(mensagem('Poxa! Você não acertou nenhuma 😕. Continue tentando!🙂'))
if acertos == 1:
    limpar_tela()
    print(mensagem('Párabens! Você acertou 1/3 😀. Continue melhorando!🙂'))
if acertos == 2:
    limpar_tela()
    print(mensagem('Párabens! Você acertou 2/3 😀. Continue melhorando!🙂'))
if acertos == 3:
    limpar_tela()
    print(mensagem('Uau! Você acertou TODAS 😁!'))