marks = int(input("Enter Marks:"))

if marks >= 90 and marks <=100:
    print("O Grade")
elif marks >= 85 and marks <= 90:
    print("A+ Grade")
elif marks >= 75 and marks <= 80:
    print("A Grade")
elif marks >= 70 and marks <= 75:
    print("B+ Grade")
elif marks >= 65 and marks <= 75:
    print("B Grade")
elif marks >= 60 and marks <= 65:
    print("c+ Grade")
elif marks >= 55 and marks <= 60:
    print("C Grade")
elif marks >= 50 and marks <= 55:
    print("D Grade")
else:
    print("F Grade")