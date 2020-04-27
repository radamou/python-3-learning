def fibonacci(n):
    a, b = 0, 1 #assign two variables at the same time
    while a < n:
        print(a, end = ',')
        a, b = b, a+b
        print()

def fibonacciWithReturn(n):
        result = []
        a, b = 0, 1
        while a < n:
                result.append(a) #or result + [a], but this one is less efficiente
                a, b = b, a + b
        return result

suite = fibonacciWithReturn(100)
print(suite)
fibonacci(2000)