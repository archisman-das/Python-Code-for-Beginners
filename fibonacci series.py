#Write a python program to find out the Fibonacci series. The series length, N will be as per user’s choice.
#Name:Archisman Das Stream:Information Technology University Roll No:10900220058
n = int(input("Enter the value of n: "))
p = int(input("Enter a number to be found: "))
a = 0
b = 1
c = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(c, end = " ")
  count += 1
  a = b
  b = c
  c = a + b
  
