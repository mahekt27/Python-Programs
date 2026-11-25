t = ()

print("1. Create Tuple")
print("2. Count")
print("3. Index")
print("4. Length")
print("5. Maximum")
print("6. Minimum")
print("7. Display")
print("8. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        l = []
        for i in range(n):
            x = int(input("Enter element " + str(i + 1) + ": "))
            l.append(x)
        t = tuple(l)

    elif choice == 2:
        x = int(input("Enter element to count: "))
        print("Count:", t.count(x))

    elif choice == 3:
        x = int(input("Enter element to find index: "))
        if x in t:
            print("Index:", t.index(x))
        else:
            print("Element not found")

    elif choice == 4:
        print("Length:", len(t))

    elif choice == 5:
        if len(t) > 0:
            print("Maximum:", max(t))
        else:
            print("Tuple is empty")

    elif choice == 6:
        if len(t) > 0:
            print("Minimum:", min(t))
        else:
            print("Tuple is empty")

    elif choice == 7:
        print("Tuple:", t)

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")