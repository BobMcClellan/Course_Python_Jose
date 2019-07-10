movies = [
    {
        'name': 'The Matrix',
        'director': 'Wachowskis',
        'Year': '1994'
    },
    {
        'name': 'The Bourne Supremecy',
        'director': 'Paul Greengrass',
        'Year': '2004'
    },

]


# Test comment

action_to_take = input("What Would you like to do?... add / va - View All / vs - View Specific: ")

if action_to_take == "vs":
    search_by = input("How would you like to search... n-Name,  d-director,  y-year: ")
    if search_by == 'n':
        moviename = input("What movie would you like to search for?: ")
        for movie in movies:
            if movie["name"] == moviename:
                print( f"The Movie you are searching for has been found.... {movie['name']}")

elif action_to_take == "add":
    moviename = input("What is the name of your movie?: ")
    director = input("Who is the director?: ")
    yr = input("What year was this movie produced?: ")

    movies.append({'name': moviename, 'director': director, 'Year': yr})

    for movie in movies:
        print(movie['name'])

elif action_to_take == "va":
    for movie in movies:
        print(movie['name'])