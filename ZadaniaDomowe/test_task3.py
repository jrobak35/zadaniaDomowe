# Zadanie 3: Testowanie API

# Korzystając z biblioteki requests, napisz skrypt, który wysyła zapytanie do publicznego API (np. SWAPI),
# analizuje odpowiedź i sprawdza, czy zwrócone dane są poprawne.
# Skrypt powinien obsługiwać różne metody HTTP oraz różne typy danych (takie jak JSON, XML).

import requests

url = "https://swapi.dev/api"
params = {"population": "1000"}

response = requests.get(url, params)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")