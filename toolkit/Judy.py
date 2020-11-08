class Math:

    @staticmethod
    def max(list1) -> float:
        my_max = list1[0]
        for m in list1:
            if m > my_max:
                my_max = m
        return my_max

    @staticmethod
    def average(list1) -> float:
        count = len(list1)
        assert count > 0
        sum = 0
        for l in list1:
            sum += l
        return sum / count


