def factorial_head(n):
    if n == 0:
        return 1
    else:
        return n * factorial_head(n-1)
result = factorial_head(5)
print(result)
