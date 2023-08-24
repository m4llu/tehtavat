hi = "liian korkea"  #Muuttujat jotka sisältää sanoja
lo = "liian matala"
mid = "sopiva"

temp = int(input("(C)Syötä lämpötila"))
hum = int(input("(%)Syötä ilmankosteus"))

if temp >= 22 and temp <= 25:
    Temp = mid
elif temp < 22:
    Temp = lo
else:
    Temp = hi
    
if hum >= 60 and hum <= 80: 
    Hum = mid
elif hum < 60:
    Hum = lo
else:
    Hum = hi
print("Lämpötila on", Temp, "ja ilmankosteus on", Hum)



