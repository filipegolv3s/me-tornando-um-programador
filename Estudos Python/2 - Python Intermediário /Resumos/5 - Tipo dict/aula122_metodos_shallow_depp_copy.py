#shallow copy - copia rasa:
import copy

dicionario1 = {
    'chave1': 12,
    'chave2': 13,
    'lista': [0, 1 ,2] #no shallow copy, ele não copia subniveis
}

dicionario2 = copy.deepcopy(dicionario1)


dicionario2['chave1'] = 123
dicionario2['lista'] = ['Mudei com deepcopy']

print(dicionario1)
print(dicionario2)