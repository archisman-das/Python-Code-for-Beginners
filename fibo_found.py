a = 0
b = 1
c = 0
n = int(input("Enter a number to check whether it is fibonacci or not:"))
if(n==0 or n==1):
    print("Yes it is in series")
else:
    while(c<n):
        c=a+b
        a=b
        b=c
    if(c==n):
        print("Yes it is in series...")
    else:
        print("No it is not in series...")