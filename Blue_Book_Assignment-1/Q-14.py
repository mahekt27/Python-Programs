age1 = int(input("Enter the age of person 1 :"))
age2 = int(input("Enter the age of person 2 :"))
age3 = int(input("Enter the age of person 3 :"))
age4 = int(input("Enter the age of person 4 :"))
age5 = int(input("Enter the age of person 5 :"))

oldest = age1

if age2 > oldest:
    oldest = age2
if age3 > oldest:
    oldest = age3
if age4 > oldest:
    oldest = age4
if age5 > oldest:
    oldest = age5

print(f"The age of the oldest person is : {oldest}")