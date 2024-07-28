year = int(input("Enter the year you want to check."))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is a Leap Year.")
    else:
      print(f"The year {year} is not a Leap Year.")
  else:
    print(f"The year {year} is a Leap Year.")
else:
  print(f"The year {year} is not a Leap Year.")