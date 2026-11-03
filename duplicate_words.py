s = input("Enter a string: ")

words = s.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print("String after removing duplicates:", " ".join(result))