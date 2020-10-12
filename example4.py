# 零錢找法
# 有不限量的1 0元 5 元 1元若干個，今有一個零錢要找開 有幾種找法。
# ex 15 元可以找成(0 0 15)(0 1 10)(0 2 5)(0 3 0)(1 0 5)(1 1 0)) 6種找法
#
def main():
    money = int(input('輸入一個數字'))
    count = 0 ;
    for i  in range(0, int(money/10)+1):
        for j in range(0,int(money/5)+1):
            for k in range(0,money+1):
                if i*10+j*5+k == money:
                    print(f'10元 *{i} 5元*{j} 1元*{k}')



if __name__ == '__main__':
    main()