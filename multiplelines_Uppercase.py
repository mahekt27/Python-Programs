# Convert multiple lines to uppercase

print("Enter lines of text (press Enter on an empty line to stop):")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line.upper())

print("Output:")

for line in lines:
    print(line)