# Zadanie 3: Testowanie API

# Korzystając z biblioteki requests, napisz skrypt, który wysyła zapytanie do publicznego API (np. SWAPI),
# analizuje odpowiedź i sprawdza, czy zwrócone dane są poprawne.
# Skrypt powinien obsługiwać różne metody HTTP oraz różne typy danych (takie jak JSON, XML).

import requests
import json

url = "https://api.tvmaze.com/singlesearch/shows"
show = input("Please input a show name.>")
params = {"q":show}
#params = {"q":"Mentalist"}
import pprint

response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    #pprint.pprint(data)
    #print(response.text)

    name = data['name']
    premiered = data['premiered']
    summary = data['summary']

    print(f"{name} premiered on {premiered}.")
    print(summary)
else:
    print(f"Error: {response.status_code}")
