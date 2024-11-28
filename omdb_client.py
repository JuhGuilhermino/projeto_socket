"""
Classe responsável pela conexão com a API e fazer uma requisição HTTP usando socket.
"""

import socket                        #importa biblioteca socket

class OMDBClient:

    API_KEY = "5511c917"  # Substitua pela sua API key do OMDB
    

    """
    Metodo construtor: incializa o cliente OMDB
    :param self: argumento usado para acessar valoresatributos e métodos da própria instância detro da classe
    """
    def __init__(self):
        self.host = "www.omdbapi.com"   
        self.port = 80                  # porta padrão HTTP
    """
    Requisição HTTP para obter informações do filme
    :param title: parâmetro de busca
    :retun: cabeçalho da mensagem HTTP (headers) e reposta da API (body)
    """
    def get_movie_data(self, title):
        endpoint = f"/?apikey={self.API_KEY}&t={title}"
        response = self._send_request(endpoint)
        if response:
            headers, body = response.split("\r\n\r\n", 1)
            return headers, body
        return None, None

    """
    Envia uma requisição HTTP usando um socket.
    :param endpoint: endereço do recurso para a API.
    :return: Resposta completa como string.
    """
    def _send_request(self, endpoint):
        # Criar o socket usando IPv4 e TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Conectar ao servidor
            client_socket.connect((self.host, self.port))

            # Criar a requisição HTTP
            request = (
                f"GET {endpoint} HTTP/1.1\r\n"
                f"Host: {self.host}\r\n"
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

            return response.decode()

        except Exception as e:
            print(f"Erro na comunicação com o servidor: {e}")
            return None

        finally:
            # Fechar o socket
            client_socket.close()
