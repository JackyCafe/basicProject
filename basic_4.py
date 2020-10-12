#再談list
a = [1,2,3]

b = a
b.append(4)
print(f'before delete a = {a}')
print(f'before delete b = {b}')
print(f'before delete a[:] = {a[:]}')
print (hex(id(a)))
print (hex(id(b)))
del a

print(f'after delete b = {b}')
# print(f'after delete a = {a}')
print (hex(id(b)))
print (hex(id(a)))

