principal = float(input("Enter the principal amount: "))
time = int(input("Enter the Time period: "))
rate = float(input("Enter the Rate of interest: "))
si = (principal*time*rate)/100
print("Simple Interest = ","%.4f"%si)