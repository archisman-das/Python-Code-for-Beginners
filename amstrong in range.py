# Program to check Armstrong numbers in a certain interval
lower = int(input("Enter the Lower range: "))
upper = int(input("Enter the upper range: "))
for num in range(lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while(temp > 0):
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if(num == sum):
       print(num,end=" ")
