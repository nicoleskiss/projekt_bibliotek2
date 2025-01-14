# ------------------------------- Information --------------------------------- #

# Projekt bibliotek, av Nicole Dvali och Leo Edling

# ---------------------------- Klassdefinitioner ------------------------------ #
class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    def __init__(self, författare, titel, utlånad=False):
        self.författare = författare
        self.titel = titel
        self.utlånad = utlånad

    # Strängrepresentation av objektet:
    def __str__(self):
        status = "utlånad" if self.utlånad else "ej utlånad"
        return f"Boken {self.titel}, skriven av {self.författare} är ({status})."

class Library:
    """ Library är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self):
        self.books = []

    # Söker på en titel:
    def hittaTitel(self, titel):
        return [bok for bok in self.books if titel.lower() in bok.titel.lower()]
    
    # Söker på en författare:
    def hittaFörfattare(self, författare):
        return [bok for bok in self.books if författare.lower() in bok.författare.lower()]

    # Lånar en bok:
    def lånaBok(self, titel):
        for bok in self.books:
            if bok.titel.lower() == titel.lower() and not bok.utlånad:
                bok.utlånad = True
                return f"Du har lånat boken '{bok.titel}'."
        return "Boken är antingen utlånad eller finns inte i biblioteket."

    # Återlämnar en bok:
    def lämnaTillbaka(self, titel):
        for bok in self.books:
            if bok.titel.lower() == titel.lower() and not bok.utlånad:
                bok.utlånad = False
                return f"Du har lämnat tillbaka boken '{bok.titel}'."
        return

    # Lägger till en ny bok:
    def läggTill(self, författare, titel):
        self.books.append(Bok(författare, titel))
        return f"Boken '{titel}' har lagts till i biblioteket."

    # Tar bort en bok:
    def taBort(self, titel):
        for bok in self.books:
            if bok.titel.lower() == titel.lower():
                self.books.remove(bok)
                return f"Boken '{titel}' har tagits bort från biblioteket."
        return "Boken finns inte i biblioteket."

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        if not self.books:
            return "Biblioteket är tomt."
        return "\n".join(str(bok) for bok in self.books)
    
    # Sorterar böcker alfabetiskt efter titel: 
    def sorteraBöcker(self):
        self.books.sort(key=lambda bok: bok.titel)
        return "Biblioteket har sorterats efter boktitlar."

# ------------------------------ Huvudprogram --------------------------------- #
# Lista på alla böcker som finns i biblioteket:
def main():
    bibliotek = Library()
    
    bibliotek.läggTill("William Shakespeare", "Romeo och Julia")
    bibliotek.läggTill("Joseph Heller", "Catch 22")
    bibliotek.läggTill("John Kennedy Toole", "A Confederacy of Dunces")
    bibliotek.läggTill("Douglas Adams", "The Hitchhikers Guide to the Galaxy")
    bibliotek.läggTill("Douglas Adams", "The Restaurant at the End of the Universe")
    bibliotek.läggTill("Douglas Adams", "Life, the Universe and Everything")
    bibliotek.läggTill("Douglas Adams", "So Long, and Thanks for All the Fish")
    bibliotek.läggTill("Douglas Adams", "Mostly Harmless")
    bibliotek.läggTill("Isaac Asimov", "I Robot")
    bibliotek.läggTill("Miguel Cervantes", "Don Quixote")
    bibliotek.läggTill("Leo Edling", "Kiss Boken")
    bibliotek.läggTill("Nicole Dvali", "Bajs Boken")
    bibliotek.läggTill("Nicole Dvali, Leo Edling", "Kiss och Bajs Boken")
    bibliotek.läggTill("F. Scott Fitzgerald", "The Great Gatsby")
    bibliotek.läggTill("Leo Tolstoy", "Anna Karenina")
    
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:

            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok
            7. Lista alla böcker                                8. Sortera böcker 
            r. Rekomenderar böcker                              q. Avsluta program
              

        ---------------------------------------------------------------------------------------
        """)

        # Menyval:
        menyVal = input("-> ")
        
        # Söker efter titel:
        if menyVal == "1":
            titel = input("Sök efter titel: ")
            resultat = bibliotek.hittaTitel(titel)
            if resultat:
                print("\n".join(str(bok) for bok in resultat))
            else: 
                print("Inga böcker hittades med titeln " + titel)
            pass
        
        # Söker efter författare: 
        elif menyVal == "2":
            författare = input("Sök efter författare: ")
            resultat = bibliotek.hittaFörfattare(författare)
            if resultat:
                print("\n".join(str(bok) for bok in resultat))
            else:
                print("Inga böcker hittades av författaren " + författare)
            pass
        
        # Lånar en bok:
        elif menyVal == "3":
            titel = input("Ange titeln på boken du vill låna: ")
            print(bibliotek.lånaBok(titel))
        
        # Återlämnar en bok:
        elif menyVal == "4":
            titel = input("Ange titeln på boken du vill återlämna: ")
            print(bibliotek.lämnaTillbaka(titel))
        
        # Lägger till en ny bok:
        elif menyVal == "5":
            författare = input("Ange författarens namn: ")
            titel = input("Ange bokens titel: ")
            print(bibliotek.läggTill(författare, titel))

        # Tar bort en bok:
        elif menyVal == "6":
            titel = input("Ange titeln på boken du vill ta bort: ")
            print(bibliotek.taBort(titel))
        
        # Lista på alla böcker:
        elif menyVal == "7":
            print(bibliotek.listaBöcker())
        
        # Sorterar böcker: 
        elif menyVal == "8":
            print(bibliotek.sorteraBöcker())
        
        # Rekomenderar böcker:
        elif menyVal == "r":
            print("Vi rekommenderar följande böcker: ")
            print("Romeo och Julia av William Shakespeare")
            print("Kiss och Bajs Boken av Nicole Dvali, Leo Edling")
            print("Don Quixote av Miguel Cervantes")
            
        # Avslutar programmet: 
        elif menyVal == "q":
            print("Avslutar programmet.")
        else:
            print("Ogiltigt val. Försök igen.")
            

print(
"""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

if __name__ == "__main__":
    main()

# Slut på kod, kiss :-) 
