# 請設計一個遞迴程式來求出最大公因數
# 輸入有2個參數 n,m
# 請求出n與m的最大公因數
# 若兩數無公因數，則顯示"兩數互質"

class Tool:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.__call__(a,b)


