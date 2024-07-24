print("Welcome to the rollercoster ride!")
height = float(input("What is your height in centimeters?"))

if height >= 120:
    print("You can ride the rollercoster!")
    age = int(input("What's your age?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
