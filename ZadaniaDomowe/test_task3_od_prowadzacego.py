import requests
import json
import pprint

planetName = input(
    "Wybierz planetę: Tatooine, Alderaan, Yavin IV, Hoth, Dagobah, Bespin, Endor, Naboo, Coruscant, Kamino.>")

if planetName == "Hoth":

    planetName = 4

else:

    planetName = 1

url = f"https://swapi.dev/api/planets/{planetName}"

response = requests.get(url, str(planetName))

if response.status_code == 200:

    data = json.loads(response.text)

    pprint.pprint(data)

else:

    print(f"Error: {response.status_code}")