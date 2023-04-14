cpf = ''
nove_digitos = 0
contador_regressivo = []
i_contador = 0

resultado = 0
while True:
    cpf = input('Digite seu cpf (somente com números): ')
    nove_digitos = cpf[:9]
    if cpf.isdigit():
        for contador in range(10, 0, -1):
            contador_regressivo.append(contador)
            

        for digito in nove_digitos:
            resultado += int(digito) * contador_regressivo[i_contador]
            i_contador += 1

        digito_1 = (resultado * 10) % 11

        # SEGUNDO TESTE:

        if digito_1 <= 9:
            print( 'Primeiro teste, passou!')
            dez_digitos = 0
            contador_regressivo_2 = []
            i_contador_2 = 0

            resultado_2 = 0

            dez_digitos = cpf[:10]

            for contador_2 in range(11, 0, -1):
                contador_regressivo_2.append(contador_2)

            
            for digito_2 in dez_digitos:
                resultado_2 += int(digito_2) * contador_regressivo_2[i_contador_2]
                i_contador_2 += 1

            digito_2 = (resultado_2 * 10) % 11

            if digito_2 <= 9:
                print('Cpf Válido!')
            else:
                print('Este cpf é inválido')


        else:
            print('Cpf falso!')

    else:
        print('Digite apenas números!: ')