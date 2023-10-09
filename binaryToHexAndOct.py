def convert(num):
    octalDigit = 0
    count = 1
    i = 0
    pos = 0
    octalArray = [0] * 32
    
    while num != 0:
        digit = num % 10
        octalDigit += digit * pow(2, i)
        i += 1
        num //= 10
        octalArray[pos] = octalDigit
        
        if count % 3 == 0:
            octalDigit = 0
            i = 0
            pos += 1
        count += 1
    
    for j in range(pos, -1, -1):
        print(octalArray[j], end='')
    
    print(",")
    
def convertToHex(binary):
    hexDigit = hex(int(str(binary), 2))
    return hexDigit[2:].upper()

binaries = [
101010,
1100011,
100110,
111000,
10110101,
1101100,
1001111,
1110010,
11001011,
1010010,
]

for binary in binaries:
    print('oct =')
    octal = convert(binary)
    print(' ')
    hexa = convertToHex(binary)
    print('hex =')
    print(hexa)
    print(' ')