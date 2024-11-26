#1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n
n = int(input("Enter a positive integer: "))
s1=0
s2=0
i=1
j=2
while(i<=n):
    s1=s1+1/i
    i=i+2
while(j<=n):
    s2=s2+1/j
    j=j+2
s=(s1-s2)
print("Result=",str(round(s,2)))