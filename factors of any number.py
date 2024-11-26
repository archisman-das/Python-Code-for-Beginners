#Print all the factors of any given number
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
a = int(input("Enter a number:"))
print("Print all factors of",a,":")
i=1
while(i<=a):
    if(a%i==0):
        print(i,end=" ")
    i=i+1

