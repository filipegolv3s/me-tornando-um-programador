def frases_com_linhas(*args):
    linhas = '-' * 30
    frases_separadas = []
    for frase_separada in args:
        frases_separadas.append(frase_separada)
    for i in range(len(frases_separadas)):
        print('{l}\n{f}\n{l}'.format(l = linhas, f = frases_separadas[i].strip('[]').strip("'").strip('"')))
        print()


#sum soma

frases = input('Digite as frases que você quer separar (use \';\' para separar): ')

frases = frases.split(';')


frases_com_linhas(*frases)