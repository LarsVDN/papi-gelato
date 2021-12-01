# Er wordt een ijssalon geopend genaamd “Papi Gelato”, het concept is heel apart: ze verkopen er alleen vanille ijs. Wel meesterlijk lekker vanille ijs, moet ik zeggen.
#
# De medewerkers van deze ijssalon hebben een strikt programma die ze moeten volgen om de klanten te voorzien van hun ijs en ze hebben jou gevraagd om dit in een programmaatje uit te werken.
#
# Als je het programmaatje opstart moet de volgende welkomstzin te zien zijn: “Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.”
#
# Stap 1 – van het stappen plan voor de werknemer is dat hij/zij vraagd: “Hoeveel bolletjes wilt u?”.
# Aan de hand van het antwoord kunnen er een aantal dingen gebeuren:
#    A. bij een getal van 1 t/m 3 ga je naar stap 2
#    B. bij een getal van 4 t/m 8 sla je stap 2 over en krijg je de tekst te zien: “Dan krijgt u van mij een bakje met {aantal} bolletjes”
#    C. bij een getal van hoger dan 8 krijg je de tekst te zien “Sorry, zulke grote bakken hebben we niet” en wordt deze stap herhaald
#    D. anders krijg je de tekst te zien: “Sorry dat snap ik niet...” en wordt deze stap herhaald
#
# Stap 2 – Nu moet de volgende vraag gesteld worden: “Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje?”
#    A. bij een keuze van A of B ga je naar stap 3
#    B. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald.
#
# Stap 3 – Als laatste krijg je te zien “Hier is uw {hoorntje/bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N)”
#    A. bij Y als als antwoord ga je terug naar stap 1 en herhaalt zich het proces
#    B. bij N als als antwoord stopt het programma en krijg je de boodschap: “Bedankt en tot ziens!”
#    C. anders krijg je de tekst te zien: “Sorry, dat snap ik niet...” en wordt deze stap herhaald
#
#
#
# Let op: Programmeer zo DRY mogelijk en gebruik duidelijke beschrijvenende namen voor je functies en variabelen.
#
#

max = 8

def error():
    print("Sorry dat snap ik niet...")

def start(): # Stap 1
    try:
        aantal = int(input("Hoeveel bolletjes wilt u? "))
        if aantal <= 3:
            bakHoorn()
        elif aantal >= 4 and aantal <= max:
            laatsteStap()
        elif aantal > max:
            print("Sorry, zulke grote bakken hebben we niet")
            start()
    except ValueError:
        print("U mag alleen cijfers invoeren")
        start()
def bakHoorn(): # Stap 2
    pass

def laatsteStap(): # Stap 3
    pass

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
start()
