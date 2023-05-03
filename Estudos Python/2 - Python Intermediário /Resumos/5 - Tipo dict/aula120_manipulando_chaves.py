chave = 'meu_nome'# definindo uma chave fora
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

del pessoa[chave2] #apagando chave

pessoa['idade'] = 18

print(pessoa)
print('\n{0}'.format(pessoa[chave])) #acessando diretamente a chave

#print(pessoa.get(chave2, 'Não existe')) #metodo get, mostra se existe (por padrao, None)
if pessoa.get(chave2) is None:
    print('Não existe mais')
else: 
    print('Existe ainda, {0}'.format(pessoa[chave2]))