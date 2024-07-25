"""
This module provides functions to fetch and process data from the Space API about planets.
"""

import requests


def fetch_planet_data():
    """
    Fetches data from the Space API and processes it to extract information about planets.
    """
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url, timeout=10)
    planets_data = response.json()['bodies']

    planet_list = []
    for planet_info in planets_data:
        if planet_info['isPlanet']:
            name = planet_info['englishName']
            mass = planet_info['mass']['massValue'] if planet_info['mass'] else 0
            orbit_period = planet_info['sideralOrbit'] if planet_info['sideralOrbit'] else 0
            planet_list.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })
    return planet_list


def find_heaviest_planet(planets_list):
    """
    Finds the heaviest planet from the list of planets.
    """
    heaviest_planet = max(planets_list, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


# Main execution
if __name__ == "__main__":
    planet_data = fetch_planet_data()
    for planet in planet_data:
        print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")

    heaviest_name, heaviest_mass = find_heaviest_planet(planet_data)
    print(f"The heaviest planet is {heaviest_name} with a mass of {heaviest_mass} kg.")
