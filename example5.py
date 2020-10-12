# 請設計一個遞迴程式來求出最大公因數
# 輸入有2個參數 n,m
# 請求出n與m的最大公因數
# 若兩數無公因數，則顯示"兩數互質"


def main():
    a = 363
    b = 231
    n = GCD(a, b)
    print("兩數互質" if GCD(a, b) == 1 else  GCD(a, b))

def GCD (a,b):
    if a % b == 0:
        return b
    else:
        return  GCD(b,a%b)



if __name__ == '__main__':
    main()