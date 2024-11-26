num1 = int(input("Enter first Positive number : "))
num2 = int(input("Enter second Positive number : "))
if(num1>num2):
    dividend=num1
    divisor=num2
else:
    dividend=num2
    divisor=num1
while(divisor!=0):
    r=dividend%divisor
    dividend=divisor
    divisor=r
print("GCD OF",num1,"and",num2,"is:",dividend)