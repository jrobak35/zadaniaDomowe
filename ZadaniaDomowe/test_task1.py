# Zadanie 1: Web Scraping

# Python jest często używany do automatycznego przeszukiwania stron internetowych,
# co jest kluczowe w wielu rolach testowania. Napisz prosty skrypt, który scrapuje dane
# z jakiejkolwiek strony internetowej. Skrypt powinien odwiedzić stronę, wydobyć
# pewne informacje (np. nagłówki artykułów), a następnie zapisać te informacje w pliku txt.

from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scrapped_quotes.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])