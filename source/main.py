from search_movie import SearchMovie #importa classe

print("=========================== MEUS FILMES ===========================")
print("1 - Buscar um filme (retorna cabeçalho HTTP + dados do filme).")
print("2 - Buscar um filme (retorna dados do filme).")
print("3 - Vizualizar filmes salvos.")
op = int(input(">>> Informe a operação desejada:  "))
print("------------------------- FICHA DO FILME --------------------------")

if op == 1:
    title = input("Informe o nome do filme:   ")

    search = SearchMovie()
    search.get_movie(title)
    search.print_header()
    print("\n")
    search.print_data()

elif op == 2:
    title = input("Informe o nome do filme:   ")

    search = SearchMovie()
    search.get_movie(title)
    search.print_data()

elif op == 3:
    print("Operação não implementada")

else: 
     print("Operação INVÁLIDA!")   
