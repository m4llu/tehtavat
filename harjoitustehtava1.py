import math 
#stores inputs to variables as integrers
a = int(input("Anna a arvo"))
b = int(input("Anna b arvo"))
c = int(input("Anna c arvo"))
#calculates b**2-4*a*c
d = (b**2) - (4*a*c)
#calculates the final equation
juuri1 = (-b-math.sqrt(d))/(2*a)
juuri2 = (-b+math.sqrt(d))/(2*a)
#prints the answer
print("Juuret ovat", juuri2, "ja", juuri1)