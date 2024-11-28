from search_movie import SearchMovie #importa classe

print("=========================== WELCOME ===========================\n")

START = input("Do you wish to search? (Y/N) :  ")

while START == "Y":
    title = input("What’s the title of the movie?  ")

    search = SearchMovie()
    search.get_movie(title)
    search.print_data()

    START = input("Do you wish to search? (Y/N) :  ")



