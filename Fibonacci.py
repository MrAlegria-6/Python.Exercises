def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a = a + b
        b = a - b

fibonacci(10)
