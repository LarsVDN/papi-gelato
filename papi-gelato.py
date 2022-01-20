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

def smaakBolletjes(aantal):
    for i in range(aantal):
        smaakKeuze = input(f"Wilt u de smaak Aardbei, Chocolade, Munt, Vanille voor bolletje {i + 1}?")
        if smaakKeuze = "a":
            pass
        pass

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
        bakHoorntje = 'bakje'
        if bolletjes <= 4:
            bakHoorntje = vraagBakHoorn(bolletjes)
        elif bolletjes > 4 and bolletjes <= 8:
            bakHoorntje = 'bakje'
        elif bolletjes > 8:
            continue
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
