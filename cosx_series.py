#cos x = 1 - x2/2! + x4/4! - x6/6! ..... 
import math
n = int(input("Enter The Range: "))
x = int(input("Enter the angle: "))
i=1
j=2
s=0
s1=0
s2=0
p = (x*3.14)/180
print("The angle in Radian:",str(round(p,2)))
while(i<=n):
     s1=s1+math.pow(p,i)/math.factorial(i)
     i=i+4
while(j<=n):
    s2=s2+math.pow(p,j)/math.factorial(j) 
    j=j+4  
s=s1-s2
print("cosx=""%.4f"%s) 