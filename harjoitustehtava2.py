def findSecond(a, b):
    first = a.find(b)
    second = a.find(b, first + 1)
    return second

# Pyydetään käyttäjältä merkkijonot a ja b
a = input("Syötä merkkijono a: ")
b = input("Syötä merkkijono b: ")

# Kutsutaan findSecond-funktio ja näytetään tokan esiintymän indeksi
secondIndex = findSecond(a, b)
print("Toisen esiintymän indeksi: ", secondIndex)