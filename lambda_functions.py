#Lambda functions
#Lambda function declaration
#lambda argument(s): expression
lambda: print("Good Afternoon Everyone!!")

greeting= lambda:print("Good Afternoon!!!")
greeting()

#lambda accepts one argument
greeting1 = lambda name : print('Hello, Hpow are you?,',name)

#lambda call
greeting1('Mahek')

add=lambda n1,n2 : n1+n2
print("Addition of two numbers = ",add(5,10))

str1="Python is dynamic typed language"
changeUpper= lambda s: s.upper()
print(changeUpper(str1))

#lmbda function can use conditional expressions
result = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(result(15))
print(result(-5))
print(result(0))

#Check even or odd

result = lambda n: "Even" if n%2 == 0 else "ODD"
n = int(input("Enter a number: "))
print(result(n))

# Check leap year or not using Lambda function

result = lambda year: "Leap Year" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "Not a Leap Year"
year = int(input("Enter a year: "))
print(result(year))

# Convert string into Title Case using Lambda function

titleCase = lambda s: s.title()
str1 = input("Enter a string: ")
print("Title Case:", titleCase(str1))

# Reverse a number using Lambda function

reverse = lambda n: int(str(n)[::-1])
num = int(input("Enter a number: "))
print("Reverse number:", reverse(num))

# Reverse a string using Lambda function

reverse = lambda s: s[::-1]
str1 = input("Enter a string: ")
print("Reverse string:", reverse(str1))

#returns true if the argument passes is even

def check_even(number):
    if number % 2 == 0:
        return True
    return False

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evenNum = filter(check_even, numbers)
# Converting to list
even_numbers = list(evenNum)
print("Even numbers:", even_numbers)