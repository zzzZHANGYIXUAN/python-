# 【例11-1】第一种函数调用
# def sing_xiaolaohu():
#     print("两只老虎两只老虎，跑得快")
#     print("一个没有尾巴，一个没有眼睛")
#     print("真奇怪")
# sing_xiaolaohu()



# 【例11-2】第二种函数调用
# def sing_happybirthday(name):
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print("Happy birthday,deat{0}".format(name))
#     print("Happy birthday to you!")
# sing_happybirthday('张三')



# 【例11-3】两个参数示例
# def sing_happywedding(name1,name2):
#     print("祝福{0}和{1}新婚快乐！".format(name1,name2))
#     print("祝福他们永结同心！")
#     print("祝福他们百通到老！")
# a='张三'
# b='李四'
# sing_happywedding(a,b)


# 【例11-4】第三种函数：无参数，有返回值
# 接收变量 = 函数名+（）
# import random
# def zhufuyu():
#     word_list=['恭喜发财','万事如意','心想事成','身体健康','合家欢乐','步步高升','日进斗金']
#     word=random.choice(word_list)
#     return word
# zhufu=zhufuyu()
# 上述方法可以接受函数的返回值
# print("过年好，祝您{}".format(zhufu))



# 【例11-5】多个返回值
# import random
# def zhufuyu2():
#      word_list=['恭喜发财','万事如意','心想事成','身体健康','合家欢乐','步步高升','日进斗金']
#      word1,word2=random.sample(word_list,2)
#      return  word1,word2
# zhufu1,zhufu2=zhufuyu2()
# print("新年好，祝您{0},{1}".format(zhufu1,zhufu2))


# 【例11-6】
# 输入三个数字a,b,c，通过函数判断是否能构成三角形。如果能，判断是哪种三角形
# 等边三角形
# 等腰三角形
# 直角三角形
# 普通三角形
# def jugment(a,b,c):
#     if (a<b+c) and (b<a+c) and (c<b+a):
#         if(1):
#             if (a == b == c):
#                 print("该三角形是等边三角形")
#             if (a == b) or (b == c) or (c == a):
#                 print("该三角形是等腰三角形")
#             if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == b ** 2 + a ** 2):
#                 print("该三角形是直角三角形")
#         else:
#             print("该三角形是普通三角形")
#     else:
#         print("不构成三角形")
# a,b,c=eval(input("请输入三个数字"))
# jugment(a,b,c)



# 【例11-7】带默认参数的函数
# 在定义函数时，有些参数可以存在默认值
# def dup(s,times=2):
#     print(s*times)
# dup('knock~')
# dup('knock~',4)
#默认参数相当于是附带了一个初始的数值



# 【例11-8】带可变数量参数的函数
# 在函数定义时，可以设计可变数量参数，通过参数前增加星号（*）实现
# def vfunc(a,*b):
#     print(type(b))
#     # 这里b的类型是元组
#     # for函数相当于是遍历元组里的每个元素
#     for n in b:
#         a +=n
#     return a
# result=vfunc(1,2,3,4,5)
# print(result)



# 【例11-9】星座运势
# 只要固定seed()函数中的参数，随机函数的结果也固定
# import random
# def jinriyunshi():
#     star,year,month,day=input("请输入星座，年，月，日（逗号隔开）:\n").split(",")
#     count = int(year)+int(month)+int(day)
#     random.seed(count)
#     a = random.randint(1,5)
#     b = random.randint(1,5)
#     c = random.randint(1,5)
#     d = random.randint(1,5)
#     e = random.randint(1,5)
#     print("{0}的今日运势如下：".format(star))
#     print("整体运势：{}".format(a))
#     print("爱情运势：{}".format(b))
#     print("事业运势：{}".format(c))
#     print("财富运势：{}".format(d))
#     print("健康运势：{}".format(e))
# jinriyunshi()

