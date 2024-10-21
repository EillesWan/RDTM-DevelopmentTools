import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def func(x,a,b,c,d):#需要拟合的函数
    return a*(x**3)+b*(x**2)+c*x+d
    
# 拟合点


x0 = np.array([0,10,20,30,60,90,120,180])
y0 = np.array([5,15,20,25,50,100,150,300])

# y0 = [i/(y0.index(i)+1) for i in y0]

funcArg, maparray= optimize.curve_fit(func, x0, y0, maxfev=500000)
a1, b1, c1, d1 = funcArg

print(funcArg) # 2.42869050e-06 6.44102976e-03 3.85771939e-01 7.71189785e+00

x1 = np.arange(300)
y1 = func(x1, a1, b1, c1, d1)

print(x0)
print(func(x0, a1, b1, c1, d1))

plt.figure()
plt.plot(x1[:], y1[:], 1.5, "#AB70FF")
plt.scatter(x0[:], y0[:], 2.5, "#121110")
plt.plot(range(300), range(300), "#FC3432")
# plt.scatter(25, 25, 25, "red")
plt.show()
