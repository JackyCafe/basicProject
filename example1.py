#靠窗 靠走道
seat = 19
if seat % 2 == 0:
    print ('靠走道' if seat%4==0 else '靠窗' )
else:
    print('靠走道' if seat % 4 == 3 else '靠窗')