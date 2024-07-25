import requests

def fetch_planet_data():
    """
    Fetches data from the Space API and processes it to extract information about planets.
    """
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_list = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else 0
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 0
            planet_list.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return planet_list

def find_heaviest_planet(planets):
    """
    Finds the heaviest planet from the list of planets.
    """
    heaviest_planet = max(planets, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

# Main execution
if __name__ == "__main__":
    planets = fetch_planet_data()
    for planet in planets:
        print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")
    
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")
