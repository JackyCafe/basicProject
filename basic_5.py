#輸入6 個數字並排序

def main():
    a = []
    for i in range(0,6):
        num = int(input('input a number'))
        a.append(num)
    a.sort()
    print(a)

if __name__ == '__main__':
    main()