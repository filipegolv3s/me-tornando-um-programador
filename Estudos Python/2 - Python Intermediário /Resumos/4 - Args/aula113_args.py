def multiplicado(*args):
    lista = []
    total = 1
    try:
        for numbers in range(len(args)):
            lista.append(int(args[numbers]))

        for i in range(len(lista)):
            if lista[i] == 0:
                continue
            total *= lista[i]
        par_or_impar = 'Par' if (total % 2 == 0) else 'Ímpar'
        print('Sua multiplicação deu: {t} e ele é: {pi}'.format(t = total, pi = par_or_impar))
    except:
        print('Digite apenas números! ')

multiplicado(1, 3, 0, 5, 1, 9)