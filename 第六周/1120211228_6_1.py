#编写程序，产生两个10以内的随机整数，以第一个随机整数为半径，第二个随机整数为高，计算并输出圆锥体的体积
import random
a=random.randint(1,10)
b=random.randint(1,10)
v=3.14*a*a*b/3
print("圆锥体的半径为："+str(a))
print("圆锥体的高为："+str(b))
print("圆锥体的体积为："+str(v))