a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))
sum = 0
#i=a
#while i<=b:
for i in range (a,b+1):
    if i > 0:
        sum = sum + i
    #i = i+1

if sum > 0 :
    print("Su of positive number is: ", sum)
else:
    print("Numbers are negative")