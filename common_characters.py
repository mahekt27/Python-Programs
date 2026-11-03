s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = ""

for ch in s1:
    if ch in s2 and ch not in common:
        common += ch

print("Common characters:", common)