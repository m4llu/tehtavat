#pyöritys vasemmalle
def rotate_left(binary, steps):
    return binary[steps:] + binary[:steps]
#pyöritys oikealle
def rotate_right(binary, steps):
    return binary[-steps:] + binary[:-steps]
#pyydetään syötteet
binary = input("Anna bitit: ")
steps = int(input("Anna pyöritysten lukumäärä: "))
direction = input("Anna pyörityksen suunta (vasen/oikea): ")
#tarkistaa kumpaan suuntaan halutaan pyörittää ja tallentaa pyöritetyt arvot muuttujaan
if direction.lower() == "vasen":
    rotated_binary = rotate_left(binary, steps)
elif direction.lower() == "oikea":
    rotated_binary = rotate_right(binary, steps)
else:   #jos syöte ei ollut vasen tai oikea, tulostetaan virheellinen  suunta
    print("Virheellinen suunta!")

print("Pyöritettynä:", rotated_binary)