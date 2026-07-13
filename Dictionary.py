import json

# dictionary to save movie
movie_list = {}

# add new movie
def add_movie():
    movie_name = input("Enter the movie name: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    actors = input("Enter the names of the actors (separated by commas): ")
    actors_list = actors.split(", ")
    
    movie_list[movie_name] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }
    
    print(f"{movie_name} has been added to the database.")

# edit movie
def edit_movie():
    movie_name = input("Enter the movie name to edit: ")
    if movie_name in movie_list:
        print(f"Current information for {movie_name}:")
        print(json.dumps(movie_list[movie_name], indent=4))
        
        # ask user for updated information
        genre = input("Enter the movie genre (or press Enter to keep current value): ")
        director = input("Enter the name of the director (or press Enter to keep current value): ")
        release_date = input("Enter the release date of the movie (YYYY-MM-DD) (or press Enter to keep current value): ")
        actors = input("Enter the names of the actors (separated by commas) (or press Enter to keep current value): ")
        actors_list = actors.split(", ")
        
        # Update the movie with the new information
        if genre:
            movie_list[movie_name]["genre"] = genre
        if director:
            movie_list[movie_name]["director"] = director
        if release_date:
            movie_list[movie_name]["release_date"] = release_date
        if actors:
            movie_list[movie_name]["actors"] = actors_list
        
        print(f"{movie_name} has been updated.")
    else:
        print(f"{movie_name} is not in the database.")

# delete movie
def delete_movie():
    movie_name = input("Enter the movie title to delete: ")
    if movie_name in movie_list:
        del movie_list[movie_name]
        print(f"{movie_name} has been deleted from the database.")
    else:
        print(f"{movie_name} is not in the database.")

# view all movies
def view_all_movies():
    print("All movies in the database:")
    for movie, info in movie_list.items():
        print(f"{movie}: {json.dumps(info, indent=4)}")

# search movies
def search_movies():
    print("Search movies in the database:")
    criteria = input("Enter the search criteria: ")
    matches = []
    for movie, info in movie_list.items():
        if criteria in movie or criteria in info["genre"] or criteria in info["director"] or criteria in info["actors"]:
            matches.append(movie)
    if matches:
        print("Matches found:")
        for match in matches:
            print(f"{match}: {json.dumps(movie_list[match], indent=4)}")
    else:
        print("No matches found.")

#  save movie to a file
def save_data():
    filename = input("Enter the filename to save to: ")
    with open(filename, "w") as file:
        json.dump(movie_list, file, indent=4)
    print("Data saved successfully.")

# load movie data from a file
def load_data():
    filename = input("Enter the filename to load from: ")
    with open(filename, "r") as file:
        data = json.load(file)
    global movie_list
    movie_list = data
    print("Data loaded successfully.")

# app start
while True:
    print("\n==== Movie Database Management System ====\n")
    print("1. Add a new movie")
    print("2. Edit an existing movie")
    print("3. Delete a movie")
    print("4. View all movies")
    print("5. Search movies")
    print("6. Save movie to file")
    print("7. Load movie from file")
    print("8. Exit\n")
    number = input("Enter a number from the list: ")

    if number == "1":
        add_movie()
    elif number == "2":
        edit_movie()
    elif number == "3":
        delete_movie()
    elif number == "4":
        view_all_movies()
    elif number == "5":
        search_movies()
    elif number == "6":
        save_data()
    elif number == "7":
        load_data()
    elif number == "8":
        exit()
    else:
        print("Invalid number. try again.")