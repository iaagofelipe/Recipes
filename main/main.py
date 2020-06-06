import requests
import PySimpleGuy as sg

# leite, ovos, manteiga, farinha -> bolo url:www.knsfksno.com

def query(name='', ingrediente='', page='1'):
    url = requests.get("http://www.recipepuppy.com/api/?", params={'i': ingrediente, "q": name, "p": page}).json()
    return url

def get_receita(ingrediente):
    results = query(name='', ingrediente=ingrediente)
    return results["results"][0]["title"]

def get_link(name):
    results = query(name)
    return results["results"][0]["href"]



