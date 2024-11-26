#Write a python program to find out the roots of a quadratic equation and also find the type of the roots.
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
import math
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
d= b*b-4*a*c
if(d>0):
    root1 = -(b + math.sqrt(d))/(2*a)
    root2 = -(b - math.sqrt(d))/(2*a)
    print("Roots are real and distinct,Root 1=",root1,"Root2=",root2)
elif(d==0):
    root1 = (-b)/(2*a)   
    root2 = root1
    print("Roots are real and equal,Root 1=",root1,"Root2=",root2) 
else:
    print("Roots are imaginary")    
    