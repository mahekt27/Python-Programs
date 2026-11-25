d = {}

print("1. Create Dictionary")
print("2. Add Element")
print("3. Update Element")
print("4. Delete Element")
print("5. Display Keys")
print("6. Display Values")
print("7. Display Items")
print("8. Get Value")
print("9. Length")
print("10. Display Dictionary")
print("11. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            d[key] = value

    elif choice == 2:
        key = input("Enter key: ")
        value = input("Enter value: ")
        d[key] = value
        print("Element added")

    elif choice == 3:
        key = input("Enter key: ")
        if key in d:
            value = input("Enter new value: ")
            d.update({key: value})
            print("Element updated")
        else:
            print("Key not found")

    elif choice == 4:
        key = input("Enter key to delete: ")
        if key in d:
            d.pop(key)
            print("Element deleted")
        else:
            print("Key not found")

    elif choice == 5:
        print("Keys:", d.keys())

    elif choice == 6:
        print("Values:", d.values())

    elif choice == 7:
        print("Items:", d.items())

    elif choice == 8:
        key = input("Enter key: ")
        print("Value:", d.get(key, "Key not found"))

    elif choice == 9:
        print("Length:", len(d))

    elif choice == 10:
        print("Dictionary:", d)

    elif choice == 11:
        print("Program ended")
        break

    else:
        print("Invalid choice")