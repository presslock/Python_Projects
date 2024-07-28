print("Thank you for choosing Python Pizza Deliveries!")
print("Please make sure you don't have any spelling errors, spaces or wrong capital letters while giving your input!")
size = input("Which size pizza do you want? Small, Medium, or Large?") 
add_pepperoni = input("Do you want pepperoni in your pizza? Yes or No") 
extra_cheese = input('Do you want extra cheese in your pizza? Yes or No') 

bill = 0 
if size == 'Small':
  bill += 15
elif size == "Medium":
  bill += 20
elif size == "Large":
  bill += 25
else:
  print("Error!! Please check the spelling or Cap letters or unwanted spaces.")

if add_pepperoni == "Yes":
  if size == "Small":
    bill += 2
  elif size == "Medium" or "Large":
    bill += 3

if extra_cheese == "Yes":
  bill += 1


print(f"Your final bill is: ${bill}.")