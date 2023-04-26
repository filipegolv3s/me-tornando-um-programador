def saudar(saudacao):
    def resultado_saudacao(nome):
        return '{s}, {n}!'.format(s = saudacao, n = nome)
    return resultado_saudacao

s1 = saudar('Boa tarde')

print(s1('Filipe'))