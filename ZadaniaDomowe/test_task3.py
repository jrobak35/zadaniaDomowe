# Zadanie 3: Testowanie API

# Korzystając z biblioteki requests, napisz skrypt, który wysyła zapytanie do publicznego API (np. SWAPI),
# analizuje odpowiedź i sprawdza, czy zwrócone dane są poprawne.
# Skrypt powinien obsługiwać różne metody HTTP oraz różne typy danych (takie jak JSON, XML).

import requests
import json
import pprint

url = "https://swapi.dev/api/planets"
planetName = input("Wybierz planetę: Tatooine, Alderaan, Yavin IV, Hoth, Dagobah, Bespin, Endor, Naboo, Coruscant, Kamino.>")
params = {"name":planetName}

response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    pprint.pprint(data)
else:
    print(f"Error: {response.status_code}")