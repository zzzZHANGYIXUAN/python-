# 复合赋值语句
# x,y=10,20
# print("x:{}".format(x))
# print("y:{}".format(y))


# 多目标赋值
# first=second=third="再坚持一下"
# print("first:{}".format(first))
# print("second:{}".format(second))
# print("third:{}".format(third))


# 复合赋值
# age=27
# print("age={}".format(age))
# age+=3
# print("age={}".format(age))


# 【例3-1】
# chinese=eval(input("请输入语文成绩："))
# math=eval(input("请输入数学成绩："))
# english=eval(input("请输入英语成绩："))
# mean=(chinese+math+english)/3
# print("你的平均成绩是：{:.1f}".format(mean))


# 【例3-2】
# r=eval(input("请输入圆的半径:"))
# area=3.14*r**2
# circumference=3.14*2*r
# print("圆的面积是：{:.2f}".format(area))
# print("圆的周长是：{:.2f}".format(circumference))


# 【例3-3】
# import  calendar
# year=eval(input("请输入年份："))
# table=calendar.calendar(year)
# print(table)


# 【例3-4】去网吧1（单分支结构）
# age=eval(input("请输入您的年龄："))
# name=str(input("请输入您的姓名："))
# if(age>=18):
#     print("{}已经成年".format(name))
#     print("欢迎来到本网吧")
# else:
#     print("未成年人不允许上网")


# 【例3-6】去网吧3（多分支结构）
# name=str(input("请输入您的姓名："))
# age=eval(input("请输入您的年龄："))
# if(age<=0):
#     print("输入错误，请重新输入！")
# elif(age>=18):
#     print("{}已经成年".format(name))
#     print("欢迎来到本网吧")
# else:
#     print("未成年人不允许上网")


# 例3-7】判断三角形（多条件判断）
#编写程序，从键盘输入三条边，判断是否能够构成一个三角形。如果能，则提示可以构成三角形；如果不能，则提示不能构成三角形。
# a=eval(input("请输入第一条边的长度："))
# b=eval(input("请输入第二条边的长度："))
# c=eval(input("请输入第三条边的长度："))
# if((a<b+c) and (b<a+c) and (c<a+b)):
#     print("{}，{}以及{}可以构成三角形".format(a,b,c))
# else:
#     print("{}，{}以及{}无法构成三角形".format(a,b,c))
#

# 【例3-8】合法结婚年龄（嵌套分支语句）
# sex=input("请输入您的性别(man or woman)：")
# age=eval(input("请输入您的年龄："))
# if(sex=='man'):
#     if(age>=22):
#         print("您已经到了法定结婚年龄")
#     else:
#         print("您未达到法定结婚年龄")
# if(sex=='woman'):
#     if(age>=20):
#         print("您已经到了法定结婚年龄")
#     else:
#         print("您未达到法定结婚年龄")


# 【例3-9】用户登录（嵌套分支语句）
# 编写程序，从键盘输入用户名和密码，要求先判断用户名再判断密码，如果用户名不正确，则直接提示用户名输入有误；如果用户名正确，则进一步判断密码，并给出判断结果的提示
# username=input("请输入用户名：")
# password=eval(input("请输入密码："))
# if(username!='admin'):
#     print("用户名错误")
# else:
#     if(password==789):
#         print("欢迎登录，管理员")
#     else:
#         print("密码错误")


# 【例3-8】多分支+嵌套
# 编写程序，开发一个小型计算器，从键盘输入两个数字和一个运算符，根据运算符（+、-、*、/）进行相应的数学运算，如果不是这4种运算符，则给出错误提示
# a=eval(input("请输入第一个数字："))
# b=eval(input("请输入第二个数字："))
# sign=input("请输入运算符号：")
# if(sign=='+'):
#     print("两数字的加法运算结果为：{}".format(a+b))
# elif(sign=='-'):
#     print("两数字的减法运算结果为：{}".format(a-b))
# elif(sign=='*'):
#     print("两数字的乘法运算结果为：{}".format(a*b))
# elif(sign=='/'):
#     if(b==0):
#         print("被除数不能为0")
#     else:
#         print("两数字的除法运算结果为：{}".format(a / b))


# BMI
# height=eval(input("请输入身高(米)："))
# weight=eval(input("请输体重(公斤)："))
# bmi=weight/(pow(height,2))
# print("你的bmi是{:.2f}".format(bmi))
#
# if bmi<18.5:
#     wto="偏瘦"
# elif bmi<25:
#     wto='正常'
# elif bmi <30:
#     wto='偏胖'
# else:
#     wto='肥胖'
#
# if bmi<18.5:
#     dom="偏瘦"
# elif bmi<24:
#     dom='正常'
# elif bmi <28:
#     dom='偏胖'
# else:
#     dom='肥胖'
#
# print("按照国际标准，你的身体状况是：{};按照国内标准，你的身体状况是：{}".format(wto,dom))


#random库
#第一种import方式
# import random
#第二种import方式
# from random import random
# from random import randint
# from random import uniform
#第三周import方式
# from random import  *
# print("随机1个[0,1)的小数:{}".format(random.random()))
# print("随机1个[1,10]的整数:{}".format(random.randint(1,10)))
# print("随机1个[1,10]的小数:{}".format(random.uniform(1,10)))


# 【例3-9】猜数字（random+分支）
# 编写程序，调用随机函数生成一个1～10之间的随机整数，从键盘输入数字进行猜谜，给出猜测结果（太大、太小、成功）的提示。
# from random import randint
# random=randint(1,10)
# number=eval(input("请输入数字："))
# if(number==random):
#     print("恭喜猜中")
# elif(number<random):
#     print("您猜的太小")
# else:
#     print("您猜的太大")
