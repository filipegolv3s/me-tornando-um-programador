import os
while True:
    cpf_do_usr = input('Digite seu cpf (sem pontos e traços): ')
    cpf_int = []

    if cpf_do_usr.isdigit():
        for i in range(len(cpf_do_usr)):
            cpf_int.append(int(cpf_do_usr[i]))

    #criando a lista dos multiplicadores
    decrescente = range(10, 0, -1)
    multiplicadore_s = []
    for multiplicador in decrescente:
        multiplicadore_s.append(multiplicador)


    sub_total = 0
    for numero_a_ser_x in range(0, 9):

        multiplicao = cpf_int[numero_a_ser_x] * multiplicadore_s[numero_a_ser_x]
    
        sub_total += multiplicao


    total = (sub_total * 10) % 11
    os.system('clear')
    if total > 9:
        print(0)
    else:
        print(f'Cpf funciona:  {total}')






