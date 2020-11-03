class Judy:

    def min(self,list1):
        min = list1[0]
        for a in list1:
            if a < min:
                min = a
        return min


list2 = [9,6,3,4,8,52,11]
judy = Judy()
min = judy.min(list2)
print(min)