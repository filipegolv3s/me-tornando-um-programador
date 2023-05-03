# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

chave = 'nome'
chave2 = 'enderecos2'

pessoa = {
    chave: 'Filipe', ## recebendo ela de forma dinamica
    'sobrenome': 'Golves',
    'enderecos': [
        {'rua1': 'tal tal', 'numero1': 23}
    ],
    chave2: [
        {'rua2': 'jjj jjj', 'numero2': 44}
    ],
}

print(pessoa.__len__())
#print(pessoa.keys())# isto não
#print(tuple(pessoa.keys())) #coerção
#print(tuple(pessoa.keys()),tuple(pessoa.values())) #= items

pessoa.setdefault('idade', 'Não definida')


for chaves, valores in pessoa.items():
    print(chaves, valores)