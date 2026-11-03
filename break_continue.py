a = int(input("Enter Starting Number:"))
b = int(input("Enter Ending Number:"))
#i=a
for i in range(a,b):
#while i <= b:
    if i % 2 == 0:
        if i == 50:
            break
        print("Value is" ,i)
    else:
        if i == 11:
            #i += 1
            continue
        print("Value is" ,i)
    #i += 1