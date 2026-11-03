#use of keyword arguments
def display(fname,lname):
    print('First Name:', fname)
    print('Last Name:', lname)
display(lname = 'KKK', fname = 'ODD')

#positional arguments
def posArfunc(name, programName):
    print("My name is : ",name)
    print("I am pursuing ",programName)
posArfunc('Mahek','MCA')

#use of arbitary arguments, program to find
def add3(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Addition = ", result)

#function call with 3 arguments
add3(11,22,33)

#function call with 2 arguments
add3(14,9)

