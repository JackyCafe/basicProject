# list
# 特點是有序，具索引，
# 內容長度可以變動

a = [1,2,3,]
#set
s = {}
print(a)
print(s)
a1 = []
for i in range(1,11):
    a1.append(i)

#
print(a1)

for i in range(0,len(a1)):
    print(a1.__getitem__(i),end='\t')

print()
for a2 in a1:
    print(a2,end='\t')

print()
print('-----index-----')
# 算第幾個元素
print(a1.index(10))

print('List pop :移除list 中其中一個index')
print(f'initial a1 {a1}' )
print(a1.pop(0))
print(f'after pop (0) {a1}' )

print('List remove:移除list 中其中一個值')
print(f'initial a1 {a1}' )
print(a1.remove(10))
print(f'after remove (0) {a1}' )

print('List 中的元素可以是 字串')
lists = ['apple','banana','orange']
for str in lists:
    print(str,end='\t')