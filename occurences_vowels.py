# Count vowels

s = input("Enter a string: ").lower()

for vowel in "aeiou":
    count = s.count(vowel)
    print(vowel, ":", count)