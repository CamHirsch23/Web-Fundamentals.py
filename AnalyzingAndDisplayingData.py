import requests

def fetch_pokemon_data(pokemon_name):
    """
    Fetches data from the Pokémon API for a given Pokémon name.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def print_pokemon_details(pokemon_data):
    """
    Prints the name, abilities, and weight of a Pokémon given its data.
    """
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    weight = pokemon_data['weight']
    print(f"Name: {name.capitalize()}, Abilities: {abilities}, Weight: {weight}")

def calculate_average_weight(pokemon_list):
    """
    Calculates the average weight of a list of Pokémon.
    """
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

# Main execution
if __name__ == "__main__":
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]
    if all(pokemon_data_list):
        for pokemon_data in pokemon_data_list:
            print_pokemon_details(pokemon_data)
        average_weight = calculate_average_weight(pokemon_data_list)
        print(f"Average Weight: {average_weight}")
