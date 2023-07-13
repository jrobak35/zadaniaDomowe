# Zadanie 1: Web Scraping

# Python jest często używany do automatycznego przeszukiwania stron internetowych,
# co jest kluczowe w wielu rolach testowania. Napisz prosty skrypt, który scrapuje dane
# z jakiejkolwiek strony internetowej. Skrypt powinien odwiedzić stronę, wydobyć
# pewne informacje (np. nagłówki artykułów), a następnie zapisać te informacje w pliku txt.

from bs4 import BeautifulSoup
import requests

testowana_strona = requests.get("https://pepper.com/")
zupa = BeautifulSoup(testowana_strona.text, "html.parser")
cytat = zupa.find("p", attrs={"class":"text-block grey-light"})

print(cytat.text)

plik = open("cytat_z_peppera.txt", "w")
plik.write(cytat.text)
plik.close()