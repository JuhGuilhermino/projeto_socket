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
        self.body = ""

    """
    Solicitação do título do filme e relaiza busca dos dados na API
    """
    def get_movie(self, title):
        self.title = title
        self.header, self.body = self.client.get_movie_data(self.title)
    
    """
    Retorna header JSON
    """
    def set_header(self):
        return self.header
    
    """
    Retorna body JSON
    """
    def set_body(self):
        return self.body

    """
    Exibir fixa tecnica do filme editada
    """
    def print_data(self):
        print("\n------------------------ HEADER HTTP ---------------------------")
        print(self.header)
        print("\n----------------------- SEARCH RESULT --------------------------")
        dados = json.loads(self.body)
        name = dados["Title"]
        print(f"Nome: {name}")
    
    
    

    