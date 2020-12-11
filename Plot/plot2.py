import matplotlib.pyplot as plt
# 參數(x,y,style) style default = 'b-'
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 20, 0, 20]) # 設定x軸與y軸範圍
plt.xlabel('x')
plt.xlabel('y=x*x')
plt.show()