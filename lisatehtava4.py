from random import randint  #random lisäosa

def arvaa_luku():   #funktion määritys
    luku = randint(1, 10)
    
    while True: #silmukka joka pyytää syötteen kunnes arvaus on oikein
        arvaus = int(input("Arvaa luku: "))
        
        if arvaus < luku:
            print("Luku on suurempi!")
        elif arvaus > luku:
            print("Luku on pienempi!")
        else:
            print("Oikein!")
            break

arvaa_luku()    #kutsutaan funktio