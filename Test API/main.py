import requests
import time

# URL de la API Rick & Morty
url = "https://rickandmortyapi.com/api/character"

# Tiempo de respuesta
start = time.time()
response = requests.get(url)
end = time.time()

# Imprimir Resultados (Tiempo Respuesta / Status Code)
print(f"Tiempo de respuesta: {end - start:.3f} segundos")
print(f"Status code: {response.status_code}")

# Validación de estructura del JSON y si contiene la lista de personajes "results"
data = response.json()
assert isinstance(data, dict), "El response no es un diccionario"
assert "results" in data, "No se encontró la clave 'results'"

# Filtrar personajes principales vivos
main_characters = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Beth Smith", "Jerry Smith"]
alive_main = [char for char in data["results"] if char["name"] in main_characters and char["status"] == "Alive"]

#Imprimir Personajes principales vivos
print("\nPersonajes principales vivos:")
for char in alive_main:
    print(f"- {char['name']} ({char['species']})")