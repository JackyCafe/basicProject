#99 乘法
for k in range(0,2):
    for i in range(1,10):
        for j in range (2,6):
            print(f'{4*k+j} * {i} = {(4*k+j)*i}',end='\t' )
        print(end='\n')
    print(end='\n')