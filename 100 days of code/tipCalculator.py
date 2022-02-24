print("Welcome to the Tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = float("1." + input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill?"))

final_bill = (total_bill * percentage) / people
final_bill = "{:.2f}".format(final_bill)

print(f"Each person should pay ${final_bill}")