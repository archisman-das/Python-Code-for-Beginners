#1+1/2!+1/3!+1/4!+....+1/n!
import math
n = int(input("Enter the range: "))
i=1
sum=0
while(i<=n):
    sum=sum+1/math.factorial(i)
    i=i+1
print(sum)
    