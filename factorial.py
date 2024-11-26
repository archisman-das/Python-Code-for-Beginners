num = 5
fact = 1

if num>0:
    while(num!=0):
        fact = fact*num
        num-=1
    print(fact)
else:
    print("No factorial found!")