s = ""

print("1. Create String")
print("2. Length")
print("3. Uppercase")
print("4. Lowercase")
print("5. Capitalize")
print("6. Title")
print("7. Count")
print("8. Find")
print("9. Replace")
print("10. Reverse")
print("11. Display String")
print("12. Exit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        s = input("Enter a string: ")

    elif choice == 2:
        print("Length:", len(s))

    elif choice == 3:
        print("Uppercase:", s.upper())

    elif choice == 4:
        print("Lowercase:", s.lower())

    elif choice == 5:
        print("Capitalize:", s.capitalize())

    elif choice == 6:
        print("Title:", s.title())

    elif choice == 7:
        x = input("Enter character or word: ")
        print("Count:", s.count(x))

    elif choice == 8:
        x = input("Enter word to find: ")
        print("Position:", s.find(x))

    elif choice == 9:
        old = input("Enter old word: ")
        new = input("Enter new word: ")
        print("Replaced String:", s.replace(old, new))

    elif choice == 10:
        print("Reverse:", s[::-1])

    elif choice == 11:
        print("String:", s)

    elif choice == 12:
        print("Program ended")
        break

    else:
        print("Invalid choice")