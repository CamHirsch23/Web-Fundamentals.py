"""
This module provides functions to fetch and process data from the Pokémon API.
"""

import requests


def fetch_pokemon_data(pokemon_name):
    """
    Fetches data from the Pokémon API for a given Pokémon name.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url, timeout=10)
    if response.ok:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None


def print_pokemon_abilities(pokemon_data):
    """
    Prints the name and abilities of a Pokémon given its data.
    """
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {name.capitalize()}, Abilities: {abilities}")


def calculate_average_weight(pokemon_list):
    """
    Calculates the average weight of a list of Pokémon.
    """
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list if pokemon)
    average_weight = total_weight / len(pokemon_list)
    return average_weight


# Main execution
if __name__ == "__main__":
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    pokemon_data_list = []

    # Fetch and print data for each Pokémon
    for pokemon_name in pokemon_names:
        data = fetch_pokemon_data(pokemon_name)
        if data:
            print_pokemon_abilities(data)
            pokemon_data_list.append(data)

    # Calculate and print the average weight
    if pokemon_data_list:
        avg_weight = calculate_average_weight(pokemon_data_list)
        print(f"Average Weight: {avg_weight}")
