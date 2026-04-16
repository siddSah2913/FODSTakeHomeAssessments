""" 9.	Write a program to ask details of 3 movies (title, director, release year, rating). 
Store them in a dictionary and display the information in a well-formatted manner.  """

def movie_details():
    movies_dict = {}
    # Loop to get details of 3 movies from the user
    for i in range(1, 4):
        print(f"\nEnter details for Movie {i}: ")
        title = input("\nTitle: ")
        director = input("Director: ")
        release_year = input("Release Year: ")
        rating = input("Rating (out of 10): ")
        
        # Adding the movie details to adictionary with the title as the key
        movies_dict[title] = {
            "Director": director,
            "Release Year": release_year,
            "Rating": rating
        }
    
    return movies_dict

# Calling the function and storing the returned dictionary
movies = movie_details()

# Printing the details of each movie in a proper format
print("\n\n----------Movie Details:----------")
for title, details in movies.items():
    print(f"\nTitle: {title.capitalize()}")
    print(f"Director: {details['Director'].capitalize()}")
    print(f"Release Year: {details['Release Year'].strip()}")
    print(f"Rating: {details['Rating'].strip()} / 10")