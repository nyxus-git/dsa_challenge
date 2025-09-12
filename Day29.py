def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev2 = 0
    prev1 = 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1

print(f"F(5) = {fibonacci(5)}")   

print(f"F(10) = {fibonacci(10)}") 

print(f"F(0) = {fibonacci(0)}")   

print(f"F(1000) = {fibonacci(1000)}") 
