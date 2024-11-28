from search_movie import SearchMovie #importa classe

print("=========================== MEUS FILMES ===========================\n")
print("------------------------------- MENU ------------------------------\n")
print("1 - Buscar um filme. \n")
print("2 - Vizualizar filmes salvos. \n")
print("3 - Sair. \n")
op = int(input(">>> Informe a operação desejada:  "))

if op == 1:
    title = input("Informe o nome do filme:   ")

    search = SearchMovie()
    search.get_movie(title)
    search.print_data()
elif op == 2:
    print("Operaçaõ não implementada")

else: 
     print("Operação INVÁLIDA!")   
