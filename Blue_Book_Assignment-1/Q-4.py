unit = int(input("Enter the unit of Electricity bill :"))

if unit <= 100:
    print("No charges is to pay")

elif unit > 100 and unit <= 200:
    bill = (unit - 100) * 5
    print("bill = ", bill)

elif unit > 200:
    bill = (100 * 0) + (100 * 5) + (unit - 200) * 10
    print("bill = ", bill)