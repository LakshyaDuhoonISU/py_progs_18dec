#pokedex
import requests
while True:
    pokemon_name = input("Enter the name of a Pokémon: ")

    # Making a request to the Poké API
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    pokemon_data = response.json()
    #print(pokemon_data)

    #Checking if the request was successful
    if response.status_code == 200:
        # Extracting information from the response
        pokemon_id = pokemon_data['id']
        pokemon_types = [type_data['type']['name'] for type_data in pokemon_data['types']]

        # Printing the information
        print('\nName:', pokemon_name.capitalize())
        print('ID:', pokemon_id)
        print('Types:', ', '.join(pokemon_types))
    else:
        print(f"Error: Unable to retrieve data for {pokemon_name}")
    a=input("Want to see more Pokemon?(y/n): ")
    if a.lower() != "y":
        break