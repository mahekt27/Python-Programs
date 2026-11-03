# Store consonants from a string

s = "Good afternoon, we are implementing strings"
vowels = "aeiouAEIOU"
deleted = ""

for ch in s:
    if ch.isalpha() and ch not in vowels:
        deleted += ch

print("Deleted consonants:", deleted)