# pyydetään käyttäjältä luku
num = int(input("Syötä alkuluku"))

# oletetaan, että luku on alkuluku
alkuluku = True

# tarkistetaan erityistapaus, kun luku on 1
if num == 1:
    print(num, "ei ole alkuluku")

# muut tapaukset, kun luku on suurempi kuin 1
elif num > 1:
    # käydään läpi luvut välillä 2 ja luku-1
    for i in range(2, num):
        # tarkistetaan, onko luku jaollinen i:llä
        if (num % i) == 0:
            alkuluku = False
            # keskeytetään silmukka kun löydetään jakaja
            break

    # tulostetaan tulos riippuen alkuluvun tilasta
    if alkuluku:
        print(num, "on alkuluku")
    else:
        print(num, "ei ole alkuluku")