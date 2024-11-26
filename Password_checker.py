Password = input("Enter Your Password: ")
if len(Password)<6:
    strength = "weak"
elif len(Password)<=10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength Is: ")