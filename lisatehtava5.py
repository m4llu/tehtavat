def rot13(text):    #määritellään funktio
    result = ""
    for char in text:   #silmukka joka toistuu jokaiselle merkille syötteessä
        if char.isalpha():
            if char.islower():  #jos merkki on pienellä kirjaimella
                ascii_offset = ord('a')
                rotated_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)     #tallentaa muuttujaan merkin joka on 13 aakkosen päässä syöte merkistä
                result += rotated_char  #liittää jokaisella silmukan toistolla käännetyt merkit yhteen muuttujaan
            else:
                ascii_offset = ord('A')
                rotated_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
                result += rotated_char
        else:
            result += char
    return result   #palauttaa käännetyn tekstin

# pyytää syötteen ja kääntää sen funktiolla
plaintext = input("Anna teksti: ")
encrypted_text = rot13(plaintext)
print("Käännetty teksti: ", encrypted_text) #tulostaa käännetyn tekstin