#Write a python program to find out the greatest among three integers.
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("a=",a)
print("b=",b)
print("c=",c)
if(a>b and a>c):
    print("a is the largest number")
elif(b>a and b>c):
    print("b is the largest number")
else:
    print("c is the largest number")