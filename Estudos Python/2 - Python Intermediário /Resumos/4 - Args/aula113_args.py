def multiplicado(*args):
    lista = []
    total = 0
    try:
        for numbers in range(len(args)):
            lista.append(int(args[numbers]))
            
        for i_v in range(len(lista)):
            if lista[i_v] == 0:
                lista.pop(lista[i_v])
        if not 0 in lista:
            total += lista[0]
            for i in range(1, len(lista)):
                total *= lista[i]
            print(total)
    except:
        print('Digite apenas números! ')

multiplicado(1, 0, 3, 4, 5)