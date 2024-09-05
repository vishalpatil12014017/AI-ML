import math

print(10 + 5**2 // 5 - 5 * 5 / 5)
# 10 + 25 // 5 - 25 / 5
# 10 + 5 - 5.0
# 10.0


## Integer
# here in python all values
# -1, 0, 10, 199023893093
# any length number will be integer there is no bigInt for long size dataType

## Float
# here in python all values having decimal are known as float
# -1.0, 0.1, 1.0, 1000.0

### non-decimal numbers (integers with no base 10)

# normal value like 1,2,3,4 known as decimal which having base value of 10 default
# any number with base value is non decimal number like 10n here value is 10 base 3
#  for converting binery to decimal we have to do some calculations like below ex. (1010)n and n=5
# 1010n = (5 is the the base)**(3 position or index of left most number from right from zero)*(1 is the value) + (5 is the the base)**(2 position or index of left most number from right from zero)*(0 is the value) +(5 is the the base)**(1 position or index of left most number from right from zero)*(1 is the value) +(5 is the the base)**(0 position or index of left most number from right from zero)*(0 is the value)
# 1010n = (5**3)*1 + (5**2)*0 + (5**1)*1 + (5**0)*0
# 1010n = 125*1 + 25*0 +5*1 + 1* 0
# 1010n = 125 + 0 + 5 + 0
# 1010n = 130
print(int("1010", 5)) # 130


## Binary to decimal
# it always base 2 of value ex. 10n where n is default 2 for binary number
# binary number are represented by 0b or 0B it starts with that value for ex. 0b1010 , 0B1010
# 0b1010 = starts with 0b means its binary
# 0b1010 = (1010)n and n = 2
# (1010)2 = (2**3)*1+(2**2)*0+(2**1)*1+(2**0)*0
# (1010)2 = 8*1+4*0+2*1
# (1010)2 = 8+0+2
# (1010)2 = 10

print(0b1010, 0B1010, int("1010", 2)) # 10 10 10


## octal to decimal
# it always base 8 of value ex. 10n where n is default 8 for octal number
# octal number are represented by 0o or 0O it starts with that value for ex. 0o1010 , 0O1010
# 0o1010 = starts with 0o means its octal
# 0o1010 = (1010)n and n = 8
# (1010)8 = (8**3)*1+(8**2)*0+(8**1)*1+(8**0)*0
# (1010)8 = 512*1+64*0+8*1+1*0
# (1010)8 = 512+0+8+0
# (1010)8 = 520

print(0o1010, 0O1010, int("1010", 8)) # 520 520 520

## hexaDecimal to decimal
# it always base 16 of value ex. 10n where n is default 16 for hexadecimal number
# hexadecimal number are represented by 0x or 0X it starts with that value for ex. 0x1010 , 0X1010
# 0x1010 = starts with 0x means its hexadecimal
# 0x1010 = (1010)n and n = 
# (1010)16 = (16**3)*1+(16**2)*0+(16**1)*1+(16**0)*0
# (1010)16 = 4096*1+256*0+16*1+1*0
# (1010)16 = 4096+0+16+0
# (1010)16 = 4112

print(0x1010, 0x1010, int("1010", 16)) # 4112 4112 4112

# Hexadecimal (Base 16) uses digits 0-9 and letters A-F, where:
# A = 10
# B = 11
# C = 12
# D = 13
# E = 14
# F = 15

# 0xff = (ff)16
# (ff)16 = (16**1)*15+(16**0)*15
# (ff)16 = 15*16+15*1
# (ff)16 = 240+15
# (ff)16 = 255

print(0xff) # 255


### Floating point dataType
# it is used to store decimal number with precision
# for ex. 1.20384950
print(1.2e2) # means wee need to multiply it by 100
print(1.2e-3) # means wee need to devide it by 1000
print(9.9999e4,9999999.9999e-5) # 99999.0 99.999999999