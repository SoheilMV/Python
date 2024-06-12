"""
In this app, we will implement a calculator with the ability to calculate
factorial sequences using recursion function!
"""
def main():
    username = input("Hello, what is your name? ")
    print(f"Welcome to our program dear {username}")
    while True:
        symbols = ["plus", "minus", "multiple", "fraction"]
        specialOperation = input()
        operation = input("Which operation do you want to do? ")
        if operation in symbols:
            simpleCalculator(symbol=operation)
            break
        

def factorial(number:int) -> int|None:
    # Recursive Function
    """This function will get a positive integer 
       from user and will return factorial of that integer!"""
    if number > 0:
        if number == 1:
            return 1
        else:
            return number * factorial(number-1)
    else:
        print("Please enter a positive integer")

def simpleCalculator(symbol:str) -> None:
    """This function will return a number based on what operation you want from it!"""
    if symbol.lower() == "plus":
        numberOne : float = float(input("Enter your number: "))
        numberTwo : float = float(input("Enter your number: "))
        print(f"Result: {numberOne + numberTwo}")
    
    elif symbol.lower() == "minus":
        numberOne : float = float(input("Enter your number: "))
        numberTwo : float = float(input("Enter your number: "))
        print(f"Result: {numberOne - numberTwo}")
    
    elif symbol.lower() == "multiple":
        numberOne : float = float(input("Enter your number: "))
        numberTwo : float = float(input("Enter your number: "))
        print(f"Result: {numberOne * numberTwo}")
    
    elif symbol.lower() == "fraction":
        numberOne : float = float(input("Enter your number: "))
        numberTwo : float = float(input("Enter your number: "))
        print(f"Result: {numberOne / numberTwo}")
        
if __name__ == "__main__":
    main()