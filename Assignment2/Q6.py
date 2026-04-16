""" 6.	Write a function that accepts two parameters: a list of countries and the country to be searched. 
The function should return the index of the country if found. Otherwise, it should return the message “Not Found in List”. """

def search_country(countries, searched_country):
    # Convert both the searched country and list items to lowercase
    countries_lower = [country.lower() for country in countries]
    searched_country_lower = searched_country.lower()
    
    if searched_country_lower in countries_lower:     # Check if the country is in the list
        index = countries_lower.index(searched_country_lower)
        return f"{searched_country.capitalize()} is found at index {index}."
    else:
        return "Not Found in List."

# List of countries to search from
countries_list = ["Nepal", "India", "China", "Pakistan", "Bangladesh", "Sri Lanka", "Indonesia", "Thailand", "South Korea", "Japan"]

#Input from the user to search for a country
searched_country = input("\nWhich country do you want to search? ").strip()

# Calling the function and displaying the result
print(search_country(countries_list, searched_country))