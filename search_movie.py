"""
Classe responsável por gerenciar a busca do filme e fornecer uma resposta 
"""
from omdb_client import OMDBClient   #importa classe que faz a requisição

import json                          #biblioteca que permite manipular dados JASON

class SearchMovie:
    """
    Método construtor - instancia um objeto OMBDClient()
    :param self: argumento usado para acessar valoresatributos e métodos da própria instância detro da classe
    """
    def __init__(self):
        self.client = OMDBClient()

    """
    Solicitação do título do filme e relaiza busca dos dados na API
    """
    def get_movie(self, title):
        self.title = title
        #self.client.get_movie_data()
        self.header, self.body = self.client.get_movie_data(self.title)
    
    """
    Tratamento da resposta 
    """

    """
    Exibir fixa tecnica do filme
    """
    def print_data(self):
        print("\n------------------------ HEADER HTTP ---------------------------")
        print(self.header)
        print("\n----------------------- SEARCH RESULT --------------------------")
        print(self.body + "\n")
    

    