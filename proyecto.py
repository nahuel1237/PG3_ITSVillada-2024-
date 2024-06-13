import requests
from tabulate import tabulate

def obtener_pokemones():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100"  
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])
    else:
        print("Error al obtener los datos de la API")
        return []

def mostrar_pokemones(pokemones):
    headers = ["ID", "Nombre"]
    tabla = []
    for index, pokemon in enumerate(pokemones, start=1):
        nombre = pokemon['name'].capitalize()
        tabla.append([index, nombre])
    print(tabulate(tabla, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    pokemones = obtener_pokemones()
    if pokemones:
        mostrar_pokemones(pokemones)