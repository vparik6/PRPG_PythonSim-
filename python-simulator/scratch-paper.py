from instructions import *  #import all functions contained in instructions.py

square = pow(199,2)
converted = format(square, '0{}b'.format(16))
print(bin(square))
print(bin(0xf000))
msb = 0xF000 & square
lsb = 0xf & square

loadupper = 0xF << 8
print('loadupper = ' + bin(loadupper))

print(bin(lsb))
print(bin(msb))
msb = msb >> 8
print(bin(msb))
seed = msb+lsb
print(bin(seed))

print(16 >> 4)
