print("1. Area of Circle")
print("2. Area of Triangle")
print("3. Area of Rectangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif choice == 2:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of Triangle =", area)

elif choice == 3:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print("Area of Rectangle =", area)

else:
    print("Invalid choice")