# Convert alternate characters to uppercase

s = input("Enter a string: ")
result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i].lower()

print("Modified string:", result)