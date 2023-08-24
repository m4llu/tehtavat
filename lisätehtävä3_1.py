first = input("Syötä ensimmäinen merkkijono")
second = input("Syötä toinen merkkijono")
if first == second[::-1]:
    print("Merkkijonot ovat toistensa käänteisjonoja")
else:
    print("Merkkijonot eivät ole toistensa käänteisjonoja")