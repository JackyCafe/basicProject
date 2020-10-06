for i in range(0,10):
    for j in range(0,10):
        isPrime = True
        v = i*10+j+1
        for k in range(2,v):
            if v%k==0 and v > k :
                isPrime = False
                break
        print(f'{v}*' if isPrime and v>1 else  f'{v}',end='\t')

    print()