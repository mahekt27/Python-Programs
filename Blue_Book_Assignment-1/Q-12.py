a = int(input("Enter the Number a = "))
b = int(input("Enter the number b = "))
c = int(input("Enter the number c = "))

if a >= b and a >= c:
    print("a is larger number")
elif b >= a and b >= c:
    print("b is larger number")
else:
    print("c is larger number")