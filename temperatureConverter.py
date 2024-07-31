import random
from colorama import Fore 

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
def temperatureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * (5/9)
    
    
    if(user_input >= 90):
       print("Fahrenheit:  ", red,"{0:4.1f}".format(user_input), black)
       print("Celsius:  ", red, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 75) & (user_input <= 89):
        print("Fahrenheit:  ", yellow,"{0:4.1f}".format(user_input), black)
        print("Celsius ", yellow,"{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 64) & (user_input <=74):
        print("Fahrenheit:  ",green,"{0:4.1f}".format (user_input), black)
        print("Celsius ", green, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input <=63):
        print("Fahrenheit: ", blue,"{0:4.1f}".format(user_input), black)
        print("Celsius ", blue,"{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)

user=float(input("Enter a temperature in Fahrenheit to convert to Celsius:  ") )

for x in range(5):
   temperatureConverter(user)
   user=float(input("Enter a temperature in Fahrenheit to convert to Celsius: ") )
