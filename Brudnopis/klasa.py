class Human:

    def __init__(self):
        imie = ''
        wiek = 0
        plec = 'm'

    def powitanie(self):
        print("Nazywam się", self.imie)

    def ile_mam_lat(self):
        print(f"Mam {self.wiek} lat")

    def jaka_plec(self):
        if self.plec == "m":
            print("Jestem mężczyzną")
        else:
            print("Jestem kobietą")