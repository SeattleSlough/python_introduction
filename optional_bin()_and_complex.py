#complex data type
# complex - combinaiton of real and imaginary number (sqrt -1)

# bin()
# bin() - returns the binary representative of the argument
print(bin(5)) # 0b101 = hex for 5 in Base2

# can reverse binary to integer by 
#   placing binary into a string inside int()
#   specify Base 2 in 2nd arg (int(arg,base=x))
print(int('0b101', 2)) # 5