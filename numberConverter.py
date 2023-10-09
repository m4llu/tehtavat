
def convert(num):
    octalDigit = 0  # initializing the octal digit variable
    count = 1  # initializing the count variable
    i = 0  # initializing the exponent variable
    pos = 0  # initializing the position variable
    octalArray = [0] * 32  # initializing an array to store the octal digits
    
    while num != 0:
        digit = num % 10  # getting the rightmost digit of the binary number
        octalDigit += digit * pow(2, i)  # converting the binary digit to octal
        i += 1  # incrementing the exponent
        num //= 10  # removing the processed digit from the binary number
        octalArray[pos] = octalDigit  # storing the octal digit in the array
        
        if count % 3 == 0:  # checking if three digits have been processed
            octalDigit = 0  # and then resetting the octal digit
            i = 0  # also resetting the exponent
            pos += 1  # moving to the next position in the array
        count += 1  # incrementing the count
    
    for j in range(pos, -1, -1):  # iterating through the array in reverse order
        print(octalArray[j], end='')  # then printing the octal digits
    
    print(",")  # and a comma at the end 
    
def convertToHex(binary):
    hexDigit = hex(int(str(binary), 2))  # converting the binary number to hexadecimal
    return hexDigit[2:].upper()  # and return the hexadecimal number in uppercase

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
    print(binary, ' =')
    print('oct =')
    octal = convert(binary)  # using the function to conver binary to octal
    hexa = convertToHex(binary)  # and the other function to convert to hex
    print('hex =')
    print(hexa) 
    print(' ')
