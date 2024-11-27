import socket

#função que faz a comunicação com a API
def get_omdb_data(api_key, title):
    # Configurações da conexão
    host = "www.omdbapi.com"
    port = 80
    endpoint = f"/?apikey={api_key}&t={title}"

    # Criar o socket usando IPV4 e TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar ao servidor
        client_socket.connect((host, port))

        # Criar a requisição HTTP
        request = (
            f"GET {endpoint} HTTP/1.1\r\n"
            f"Host: {host}\r\n"
            f"Connection: close\r\n"
            f"\r\n"
        )
        # Enviar a requisição
        client_socket.sendall(request.encode())

        # Receber a resposta
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data

        # Processar a resposta
        response = response.decode()
        headers, body = response.split("\r\n\r\n", 1)
        return headers, body

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        # Fechar o socket
        client_socket.close()

# Configuração
API_KEY = "5511c917"  # Substitua pela sua API key do OMDB
movie_title = "Barbie"

# Obter dados do filme
headers, body = get_omdb_data(API_KEY, movie_title)

# Exibir o resultado
print("=== Cabeçalhos ===")
print(headers)
print("\n=== Corpo ===")
print(body)
