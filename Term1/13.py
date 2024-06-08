import emoji
import os
import platform
import sys

osName = platform.system()
if osName == "Windows":    
    os.system("cls")
else:
    os.system("clear")
    
while True:
    originalSentence : str = input("Enter your sentence: ")
    modifiedSentence : str = emoji.emojize(string=originalSentence, language="alias")
    print(modifiedSentence)
    anotherTime : str = input("Do you want to continue? ").lower()
    if anotherTime.startswith("n"):
        break
    
sys.exit("Thank you for using our app!")
