#Check for any given number is Armstrong or not
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
sum = 0
digit = 0
n = int(input("Enter a number: "))
num = n
num1 = n
while(n>0):
    r=n%10
    digit=digit+1
    n=n//10
while(num>0):
    r=num%10
    sum=sum+(r**digit)
    num=num//10
if(sum==num1):
    print(f"{num1} is Amstrong number")
else:
    print(f"{num1} is not Amstrong number")

