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
