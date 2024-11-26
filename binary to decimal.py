binary = int(input("Enter a Binary number: "))
deci=0
i = 0
while(binary>0):
    r=binary%10
    deci = deci+r*(2**i)
    binary = binary//10
    i = i+1
print("The Decimal Equivalent number=",deci)