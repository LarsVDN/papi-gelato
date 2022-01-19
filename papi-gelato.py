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

max = 8

def error():
    print("Sorry dat snap ik niet...")

def vraagBolletjes():
    aantalok = False
    while not aantalok:
        try:
            aantal = int(input("Hoeveel bolletjes wilt u? "))
            if aantal > max:
                print("Sorry, zulke grote bakken hebben wij niet")
            aantalok = True
        except ValueError:
            print("U mag alleen cijfers invoeren")

    return aantal

def vraagBakHoorn(aantal):
    a = 'hoorntje'
    b = 'bakje'

    while True:
        vraagHB = input("Wilt u deze " + str(aantal) + " bolletje(s) in een hoorntje of een bakje? ")

        if vraagHB in [a,b]:
            return vraagHB
        else:
            print("U mag alleen 'hoorntje' of 'bakje' invoeren")

def main(): # Stap 1
    while True:
        bolletjes = vraagBolletjes()
        if bolletjes <= 4:
            bakHoorntje = vraagBakHoorn(bolletjes)
        elif bolletjes > 4 and bolletjes <= 8:
            bakHoorntje = 'bakje'
        elif bolletjes > 8:
            return
        bakHoorntje = 'bakje'
        meerBestellen = input("U krijgt van mij een " + bakHoorntje + " met " + str(bolletjes) + " bolletjes. \n" + "Wilt U nog meer bestellen? (Y/N) ")
        if meerBestellen in ['n','N']:
            print("Tot ziens!")
            return



print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
main()









# if aantal <= 3:
#     bakHoorn()
# elif aantal >= 4 and aantal <= max:
#     laatsteStap()
# elif aantal > max:
#     print("Sorry, zulke grote bakken hebben we niet")
#     start()

# if aantal >=4 and aantal <=max:
#     print("Dan krijgt u van mij een " + str(b) + " met " + str(aantal) + " bolletjes")
# elif aantal > max:
#     print("Sorry, zulke grote bakken hebben wij niet")
