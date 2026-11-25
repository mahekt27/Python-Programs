list1 = []

print("1. Create List")
print("2. Append")
print("3. Insert")
print("4. Remove")
print("5. Pop")
print("6. Sort")
print("7. Reverse")
print("8. Search")
print("9. Display")
print("10. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        for i in range(n):
            x = int(input("Enter element: "))
            list1.append(x)

    elif choice == 2:
        x = int(input("Enter element: "))
        list1.append(x)
        print("Element added")

    elif choice == 3:
        pos = int(input("Enter position: "))
        x = int(input("Enter element: "))
        list1.insert(pos, x)
        print("Element inserted")

    elif choice == 4:
        x = int(input("Enter element to remove: "))
        list1.remove(x)
        print("Element removed")

    elif choice == 5:
        if len(list1) > 0:
            print("Removed element:", list1.pop())
        else:
            print("List is empty")

    elif choice == 6:
        list1.sort()
        print("List sorted")

    elif choice == 7:
        list1.reverse()
        print("List reversed")

    elif choice == 8:
        x = int(input("Enter element to search: "))
        if x in list1:
            print("Element found")
        else:
            print("Element not found")

    elif choice == 9:
        print("List:", list1)

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")