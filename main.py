from omdb_client import OMDBClient #importa classe

API_KEY = "5511c917"  # Substitua pela sua API key do OMDB
movie_title = "Barbie"

# Criar uma instância do cliente e obter os dados do filme
client = OMDBClient(API_KEY)
headers, body = client.get_movie_data(movie_title)

# Exibir o resultado
print("=== Cabeçalhos ===")
print(headers)
print("\n=== Corpo ===")
print(body)