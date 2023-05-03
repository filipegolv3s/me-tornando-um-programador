chave1 = 'nome'

p1 = {
    chave1: 'Filipe',
    'idade': 18,
}
    
print(p1.get(chave1))
print(p1.get('chave2', 'Aparece None'))
'''
p1.update({
    'endereco': 'rua tal',
})
'''
p1.update(endereco= 'Rua tal')
print(p1)