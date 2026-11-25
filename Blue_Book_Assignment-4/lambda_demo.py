# Lambda function: square of a number, also using map() and filter()

# 1. Lambda function
square = lambda x: x * x
n = int(input("Enter a number: "))
print("Square using lambda:", square(n))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)

# 2. Using map() with lambda
squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)

# 3. Using filter() with lambda (squares that are even)
even_squares = list(filter(lambda x: x % 2 == 0, squares))
print("Even squares using filter():", even_squares)