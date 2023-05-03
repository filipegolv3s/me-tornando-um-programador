#pessoa2 = dict(nome='Filipe', sobrenome = 'Golves')
#print('Pessoa2: {p2}'.format(p2 = pessoa2['nome']))

pessoa = {
    'nome': 'Filipe',
    'sobrenome': 'Golves',
    'enderecos': [
        {'rua1': 'tal tal', 'numero1': 23}
    ]
}



for chave in pessoa:
    print('{c} = {p}'.format(c = chave, p = pessoa[chave]))
    