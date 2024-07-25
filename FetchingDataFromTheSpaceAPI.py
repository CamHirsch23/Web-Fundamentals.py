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
    planets = response.json()['bodies']

    # Process each planet's info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] if planet['mass'] else 'N/A'
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'N/A'
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")


fetch_planet_data()
