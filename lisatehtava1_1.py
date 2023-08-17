import math #imports math functions
x1 = float(input("Syötä piste x1")) #takes input as float and stores it in var
y1 = float(input("Syötä piste y1"))
x2 = float(input("Syötä piste x2"))
y2 = float(input("Syötä piste y2"))
length =math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #line length equation
print(length)