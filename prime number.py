n = int(input("Enter a positive number:"))
flag = 0
for i in range(1,n+1):
    if(n%i==0):
        break
if(flag==2):
    print("The number is prime")
else:
    print("The number is not prime")