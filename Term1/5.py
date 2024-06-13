age = int(input("سن خود را وارد کنید: "))
if age >= 18:
    print("شما می‌توانید گواهینامه دریافت کنید.")
elif age <= 0:
    print("سن خود را درست وارد کنید.")
else:
    year = 18 - age
    print(f"شما {year} سال بعد می‌توانید اقدام به دریافت گواهینامه کنید.")


email = "admin@poulstar.org"
passs = "1234"
enterEmail = input("Please enter your email: ")
if "@gmail.com" in enterEmail:
    print("Invalid Email!")
elif email == enterEmail:
    enterPass = input("Please enter your password: ")
    if passs == enterPass:
        print("Login!")
    else:
        print("Invalid Password!")
else:
    print("You need to signup first!")

#=============================================================

grade = 5
result = input("Where is the capital of Brazil?")
if result.lower() == "rio":
    print("rio -> valid")
else:
    print("invalid")
    grade = grade - 1

result = input("Where is the capital of Germany?")
if result.lower() == "berlin":
    print("berlin -> valid")
else:
    print("invalid")
    grade = grade - 1
    
result = input("Where is the capital of Italy?")
if result.lower() == "rome":
    print("rome -> valid")
else:
    print("invalid")
    grade = grade - 1
    
result = input("Where is the capital of France?")
if result.lower() == "paris":
    print("paris -> valid")
else:
    print("invalid")
    grade = grade - 1
    
    
result = input("Where is the capital of Japon?")
if result.lower() == "tokyo":
    print("tokyo -> valid")
else:
    print("invalid")
    grade = grade - 1
    
print(f"Grade: {grade}")