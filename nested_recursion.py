def nested_recursion(n):
    if n <= 0 :
        return 1
    else:
        return nested_recursion (n-nested_recursion(n-1))
result = nested_recursion(3)
print(result)

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
print(is_even(10))
print(is_odd(10))