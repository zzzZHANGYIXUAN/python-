#编写程序，从键盘输入数字n，通过循环计算1~n的乘积
a=int(input("请输入数字："))
product=1
while(a>=1):
    product=product*a
    a=a-1
print("运算的结果是："+str(product))
