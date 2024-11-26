n = int(input("Enter a number: "))
reverse = 0
while(n!=0):
    r = n%10
    reverse = reverse*10+r
    n = n//10
print("Reverse of the number is:",reverse)