a = int(input("Enter Strating Number: "))
b = int(input("Enter Ending Number: "))

print("ODD Numbers: ")

while a<= b:
    if a % 2 != 0:
        print(a)
    a = a + 1