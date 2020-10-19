def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


def min(a)->int:
    assert type(a) == list
    minmun = a[0]

    for i in range(1,len(a)):
        if a[i]<minmun:
            minmun = a[i]
    return minmun


def max(a)->int:
    assert type(a) == list
    maxmun = a[0]
    for i in range(1, len(a)):
        if a[i] > maxmun:
            maxmun = a[i]
    return maxmun


#bobbleSort  from min to max
def sort(a)->list:
    assert type(a) == list

    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
                if a[j]> a[j+1]:
                    a[j+1],a[j] = swap(a[j+1],a[j])
                    print(i,a)

    return a


#bobbleSort  from min to max
# def sort(a)->list:
#     assert type(a) == list
#     for i in range(len(a)-1,0,-1):
#         for j in range(0,i):
#                 if a[j]> a[j+1]:
#                     a[j+1],a[j] = swap(a[j+1],a[j])
#                     print(i,a)
#
#     return a



def sort(a)->list:
    assert  type(a) == list
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j+1]<a[j]:
                a[j+1],a[j] =swap(a[j+1],a[j])
                print(f'i = {i},j ={j},a = {a}')
    return a


a = [5,3,8,7,6,4,1]
# print(a)
# b = sort(a)
# print(b)
my_min = min
print(my_min(a))

