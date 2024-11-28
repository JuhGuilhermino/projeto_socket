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
        self.header, self.body = self.client.get_movie_data(self.title)

    """
    Exibe cabeçalho da mensagem do HTTP
    """
    def print_header(self):
        print(self.header)

    """
    Exibe dados do filme
    """
    def print_data(self):
        dados = json.loads(self.body)

        title = dados["Title"]
        year = dados["Year"]
        genre = dados["Genre"]
        director = dados["Director"]
        language = dados["Language"]
        plot = dados["Plot"]

        print(f"Title: {title} \nYear: {year} \nGenre: {genre} \nDirector: {director} \nLanguage: {language} \nPlot:\n    {plot}\n\n")
    
    

    