def odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

odd_numbers(start, end)