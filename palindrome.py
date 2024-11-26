n = int(input("Enter a number: "))
p = n
reverse = 0
while(n!=0):
    r = n%10
    reverse = reverse*10+r
    n = n//10
if(p==reverse):
    print(f"{p} is palindrome")
else:
    print(f"{p} is not palindrome")