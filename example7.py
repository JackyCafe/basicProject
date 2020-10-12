# 因式分解
# ex 12 = 2*2*3
def main():
    n = int(input ('input a number'))
    k = 2;
    while n >=2 :
        if n%k == 0:
            if n == k:
                print(f'{k}', end='')
            else:
                print(f'{k}*',end='')
            n = n / k
        else:
            k += 1

if __name__ == '__main__':
    main()