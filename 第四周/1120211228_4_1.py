#编程实现，从键盘输入一个5位数字，分别输出它的个位数和千位数
number=int(input("请输入5位数字："))
number_1000=number%10000//1000
number_1=number%10
print("数字的千位是："+str(number_1000))
print("数字的个位是："+str(number_1))

