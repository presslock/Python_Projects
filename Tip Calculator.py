billamount = float(input("What was your total bill? $"))
tippercent = float(input("How much tip percentage you would like to give?? 5 , 10 , 12 , or 15?"))
people = int(input("How many people to split the bill?"))

tiponbill = billamount * (tippercent/100)

billwithtip = billamount + tiponbill

perperson = billwithtip/people
final_amount = "{:.2f}".format(perperson)

print(f"Each person should pay: ${final_amount} ")