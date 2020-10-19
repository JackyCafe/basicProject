

def swap(a,b):
    temp = a
    a = b
    b = temp
    return  a,b
a = 10
b = 3
print(f'a = {a} b = {b}')
a,b = swap (a,b)
print(f'a = {a} b = {b}')


