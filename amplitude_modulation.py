# -*- coding: utf-8 -*-
from math import sin # из библиотеки math импортируется sin
import matplotlib.pyplot as gph #импортируется библиотека mathplotlib

x = []
y = []
t = 5 # введенный параметр
a = 22 #не должен быть 0 иначе будет линия
b = 1
c = 0.1
step = 12 # шаг графика
start = 0
end = 800
t = start


while t < end :
    touch = a*sin(b*t + c)
    y.append(touch)
    x.append(t)
    
    t = t + step
#расчитали точку, задали её координаты и рисуем

#print x
#print y
gph.plot(x, y)
gph.show()
