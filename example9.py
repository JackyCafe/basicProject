#0 1 1 2 3 5 8 ....
def fib(n):
    a, b = 0 ,1
    result = []
    for i in range(n):
        sum = a + b
        a = b
        b = sum
        result.append(sum)
    return  result

print(fib(5) )