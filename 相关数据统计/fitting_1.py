import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
 
def func(x,w,h,k):#需要拟合的函数
    return np.exp(k/(x+w)+h)
    
# 拟合点
a = {20230201: 2016, 20230101: 2015, 20221201: 2014, 20221101: 2013, 20221001: 2013, 20220901: 2013, 20220801: 2012, 20220701: 2005, 20220601: 2002, 20220501: 2000, 20220401: 1995, 20220301: 1989, 20220201: 1986}

x0 = list(range(len(a)))
y0 = list(a.values())
last = y0[-1]
y0 = [(i-y0[y0.index(i)+1]) if not y0.index(i) == len(y0)-1 else 0 for i in y0]

funcArg, maparray= optimize.curve_fit(func, x0, y0)
w4, h4, k4 = funcArg
x4 = np.arange(1, 6, 0.01)
y4 = np.exp(k4/(x4+w4)+h4)

plt.figure()
plt.scatter(x0[:], y0[:], 2.5, "#121110")  
plt.scatter(25, 25, 25, "red")  
plt.plot(x4, y4, "purple")
plt.show()
