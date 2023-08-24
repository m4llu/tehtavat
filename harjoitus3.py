decimal = 0
binary = input("Anna 4-bittinen binääriluku")   #Pyydetään syöte
if len(binary) == 4:                            #Jos syötteen pituus = 4:
    for digit in binary:                        #Silmukka, joka toistuu jokaisella syötteen merkillä
        decimal = decimal*2 + int(digit)        #Muuttaa binääriluvun desimaaleiksi silmukan avulla
    print(decimal)
else:
    print("Syötteesi ei ollut nelimerkkinen")

    