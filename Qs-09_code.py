#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(n>=10 and i<10):
        print(end = " ")
    for _ in range(1,n+1-i):
        print(end = " ")
    for j in range(1,(2*i)):
        if(j==1 or j==(2*i)-1):
            print(i,end="")
        else:
            print("*",end="")
    print("")