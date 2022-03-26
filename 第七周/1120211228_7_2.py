# 编写程序，通过循环计算全部水仙花数，并依次输出。水仙花数是一个三位数字，该数字等于组成该三位数的各位数字的立方和。例如13+53+33=153
for a in range(0,10):
     for b in range(0,10):
         for c in range(0,10):
            jugment=a*a*a+b*b*b+c*c*c
            if(jugment==a*100+b*10+c and 0<jugment<1000):
                 print(str(a)+str(b)+str(c)+"是水仙花数")
