import re
import sys

cpf = re.sub(
    r'[^0-9]',
    '',
    input('Digite seu cpf(sem pontos): ')
)
caracteres_repitidos = cpf == cpf[0] * len(cpf)
# cpf = input('Digite seu cpf(sem pontos): ').replace('.', '').replace('-', '').replace(' ', '')
if caracteres_repitidos:
    print('Você digitou dados repetidos.')


nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

tratando_digito_1 = (resultado * 10) % 11
digito_1 = tratando_digito_1 if tratando_digito_1 <= 9 else 0


dez_digitos = cpf[:9] + str(tratando_digito_1)
segundo_contador_regressivo = 11

segundo_resultado = 0
for digito in dez_digitos:
    segundo_resultado += int(digito) * segundo_contador_regressivo
    segundo_contador_regressivo -= 1

tratando_digito_2 = (segundo_resultado * 10) % 11
digito_2 = tratando_digito_2 if tratando_digito_2 <= 9 else 0

cpf_recriado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_recriado == cpf:
    print('{c1} é um cpf válido!'.format(c1 = cpf))
else:
    print('{c1} é um cpf inválido!'.format(c1 = cpf))