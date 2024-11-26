deci = int(input("Enter a decimal number: "))
binary=0
i = 0
while(deci>0):
    r=deci%2
    binary = binary+r*(10**i)
    deci = deci//2
    i = i+1
print("The Binary Equivalent number=",binary)