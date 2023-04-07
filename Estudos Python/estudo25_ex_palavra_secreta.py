import os
palavra_secreta = 'Interstellar'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_chutada = input('Digite uma letra: ')
    numero_tentativas += 1

    #Se tudo ocorrer bem, essa função abaixo será ignorada, se o usuário digitar mais de uma letra, ela será executada.
    if len(letra_chutada) > 1:
        print('Digite apenas uma letra!')
        continue

    #1- Descobrir se a letra chutada está na palavra secreta:
    if letra_chutada in palavra_secreta:
        letras_acertadas += letra_chutada

    #3
    palavra_completa = ''

    #for faz um loop da função toda, mas pra cada letra. Ou seja, ele começa na primeira, ver se o if vai rodar, se não rodar, vai para o else. #2
    for letra_apagada in palavra_secreta:
        if letra_apagada in letras_acertadas:
            palavra_completa += letra_apagada
        else:
            palavra_completa += '*'

    print('Palavra formada: {0}'.format(palavra_completa))

    if palavra_completa == palavra_secreta:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('Parabéns! Você acertou.')
        print('A palavra era: {}'.format(palavra_secreta))
        print('Tentativas: {}'.format(numero_tentativas))
        #reiniciar o codigo
        letras_acertadas = ''
        numero_tentativas = 0