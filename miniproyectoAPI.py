import requests
from flask import Flask, render_template_string

# Inicia la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    # Solicitud GET a la PokeAPI para obtener información sobre los primeros 10 Pokémon
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    data = response.json()["results"]

    # Crea una plantilla HTML para mostrar los datos en una tabla
    html_content = """
    <h1>Lista de Pokémon</h1>
    <table border="1">
      <tr>
        <th>Nombre</th>
        <th>URL</th>
      </tr>
      {% for pokemon in data %}
      <tr>
        <td>{{ pokemon['name'] }}</td>
        <td>{{ pokemon['url'] }}</td>
      </tr>
      {% endfor %}
    </table>
    """
    
    # Renderiza la tabla con los datos de Pokémon
    return render_template_string(html_content, data=data)

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)