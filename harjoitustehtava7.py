#Tuodaan random kirjasto
import random
#funktio jonka avulla tarkistetaan miten monella rivillä oli 4, 5, 6 tai 7 oikein
def lotto_arvonta(lottorivi, maara):                      
    oikeat_numerot = []
    #silmukka toistuu niin monta kertaa kun käyttäjä haluaa arpoa
    for i in range(maara):
        arvottu_rivi = []
        #silmukka arpoo lottonumeron 7 kertaa
        for j in range(7):
            arvottu_numero = random.randint(1, 39)
            arvottu_rivi.append(arvottu_numero)
        #vertaa lottorivejä keskenään
        oikeat_luvut = set(lottorivi) & set(arvottu_rivi)
        
        if len(oikeat_luvut) == 4:
            oikeat_numerot.append("neljä")
        elif len(oikeat_luvut) == 5:
            oikeat_numerot.append("viisi")
        elif len(oikeat_luvut) == 6:
            oikeat_numerot.append("kuusi")
        elif len(oikeat_luvut) == 7:
            oikeat_numerot.append("seitsemän")
            
    return oikeat_numerot
#pyytää lottorivin käyttäjältä ja muuttaa sen listaksi
lottorivi = input("Anna lottorivi (erottele numerot pilkulla): ").split(",")
lottorivi = [int(numero) for numero in lottorivi]
#pyytää määrän kuinka monta kertaa rivejä arvotaan
maara = int(input("Kuinka monta riviä arvotaan: "))

oikeat_numerot = lotto_arvonta(lottorivi, maara)

print(oikeat_numerot.count("neljä"), "kertaa neljä oikein!")
print(oikeat_numerot.count("viisi"), "kertaa viisi oikein!")
print(oikeat_numerot.count("kuusi"), "kertaa kuusi oikein!")
print(oikeat_numerot.count("seitsemän"), "kertaa seitsemän oikein!")