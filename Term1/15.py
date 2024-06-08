"""
In this project, we will use the BMI formula to determine
how you should plan your diet!
You'll need to give your height in meters & your weight in kilograms
to the machine to calculate your BMI!
"""
# Importing modules
import time

# Getting Inputs
def main() -> None:
    username : str = input("Enter your username: ")
    height : float = float(input("Height(Meters): "))
    weight : float = float(input("Weight(Kilograms): "))
    formula(username, height, weight)
    
# Calculating the formula
def formula(username:str, height:float, weight:int|float) -> None:
    print(f"Dear {username}, please pay attention!")
    
    for i in range(3): # 1-2-3
        print((i+1) * ".")
        time.sleep(0.75)
        
    userBodyMassIndex = weight / (height ** 2)
    idealWeight = 22*(height ** 2)
    
    if userBodyMassIndex > 25:
        weightLoss = weight - idealWeight
        print(f"You are over weighted!\nYou need to lose {weightLoss} Kgs!")
    elif userBodyMassIndex < 19:
        weightGain = idealWeight - weight
        print(f"You are under weighted!You need to lose {weightGain} Kgs!")
    else:
        print("You are a nice fit!")

if __name__ == "__main__":
    main()
    
    