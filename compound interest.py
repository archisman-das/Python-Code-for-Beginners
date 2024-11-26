p = float(input("Enter the principal amount: "))
t = int(input("Enter the Time period: "))
r = float(input("Enter the Rate of interest: "))
ci = (p*(1+r/100)**t)-p
print("Compound interest = ","%.4f"%ci)