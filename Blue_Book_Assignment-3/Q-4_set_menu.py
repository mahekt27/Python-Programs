s = set()

print("1. Create Set")
print("2. Add Element")
print("3. Remove Element")
print("4. Discard Element")
print("5. Pop Element")
print("6. Union")
print("7. Intersection")
print("8. Difference")
print("9. Length")
print("10. Display Set")
print("11. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        for i in range(n):
            x = int(input("Enter element: "))
            s.add(x)

    elif choice == 2:
        x = int(input("Enter element: "))
        s.add(x)
        print("Element added")

    elif choice == 3:
        x = int(input("Enter element to remove: "))
        if x in s:
            s.remove(x)
            print("Element removed")
        else:
            print("Element not found")

    elif choice == 4:
        x = int(input("Enter element to discard: "))
        s.discard(x)
        print("Element discarded")

    elif choice == 5:
        if len(s) > 0:
            print("Removed element:", s.pop())
        else:
            print("Set is empty")

    elif choice == 6:
        s2 = {4, 5, 6}
        print("Second Set:", s2)
        print("Union:", s.union(s2))

    elif choice == 7:
        s2 = {4, 5, 6}
        print("Second Set:", s2)
        print("Intersection:", s.intersection(s2))

    elif choice == 8:
        s2 = {4, 5, 6}
        print("Second Set:", s2)
        print("Difference:", s.difference(s2))

    elif choice == 9:
        print("Length:", len(s))

    elif choice == 10:
        print("Set:", s)

    elif choice == 11:
        print("Program ended")
        break

    else:
        print("Invalid choice")