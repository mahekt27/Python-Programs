#tail recursion

def factorial_tail(n, result=1):
    if n == 0 :
        return result
    else:
        return factorial_tail(n-1, n * result)
    
result = factorial_tail(5)
print(result)