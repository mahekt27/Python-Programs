
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range(a,b+1):
    if i%2==0:
        if i==50:
            break
        print("Value is ",i)

    else:
        if i==11:
            continue
        print("Value is ",i)

else:
    print("Even Odd Program")


a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

sum = 0

for i in range(a, b + 1):
    if i > 0:
        sum = sum + i

if sum > 0:
    print("Sum of positive numbers is:", sum)
else:
    print("Numbers are negative")

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

sum = 0

while a <= b:
    if a > 0:
        sum = sum + a
    a = a + 1

if sum > 0:
    print("Sum of positive numbers is:", sum)
else:
    print("Numbers are negative")


list1= [27,4,6,8,2.2,4.5,3.0]
print(list1)
print(list1[5])
print(list1[-3:-1])
print(list1[1:5])