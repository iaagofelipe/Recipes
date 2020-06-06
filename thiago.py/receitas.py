import requests

leitura = open('ingredientes.txt', 'r')
escrita = open('receitas.csv', 'w')

"""Pega o numero de linhas do arquivo"""
n_linhas = sum(1 for linha in leitura)


def query(name='', ingrediente='', page='1'):
    r = requests.get("http://www.recipepuppy.com/api/?", params={'i': ingrediente, "q": name, "p": page}).json()
    return r


def get_receita(ingrediente):
    results = query(name='', ingrediente=ingrediente)
    return results["results"][0]["title"]


def get_link(name):
    results = query(name)
    return results["results"][0]["href"]


ing = leitura.readline()

receita = get_receita("eggs")
link = get_link(receita)

print(receita)
print(link)
