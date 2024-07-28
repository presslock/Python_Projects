print("Thank you for choosing Python Pizza Deliveries!")
print("Please make sure you don't have any spelling errors, spaces and write the letters in all CAPS!")
size = input("Which size pizza do you want? S, M, or L?") 
add_pepperoni = input("Do you want pepperoni in your pizza? Y or N") 
extra_cheese = input('Do you want extra cheese in your pizza? Y or N') 

bill = 0 
if size == 'S':
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("Error!! Please check the spelling or Cap letters or unwanted spaces.")

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size == "M" or "L":
    bill += 3

if extra_cheese == "Y":
  bill += 1


print(f"Your final bill is: ${bill}.")
