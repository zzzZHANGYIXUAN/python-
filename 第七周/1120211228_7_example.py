# 例3-1】自然数之和（for+range
# 编写程序，使用for语句计算1～10000的自然数之和。
# sum=0
# for i in range(10001):
#     sum=sum+i
# print("1到10000的数字之和为：{}".format(sum))


# 【例3-2】自然数偶数之和（for+range）
# 编写程序，使用for语句计算1～10000的偶数自然数之和。
# sum=0
# for i in range(10001):
#     if(i%2==0):
#         sum=sum+i
# print("1到10000的偶数数字之和为：{}".format(sum))
# sum2=0
# for i in range(2,10001,2):
#     sum2=sum+i
# print(sum2)


# 【例3-3】统计字符出现次数
# 统计“山”出现次数
# number=0
# word='山羊上山山碰山羊角'
# for i in word:
#     if i == '山':
#         number=number+1
# print("山字的数量是：{}".format(number))


# 【例3-4】凯撒密码
# plaincode=input("请输入明文：")
# for p in plaincode:
#     if ord("a") <= ord(p) <= ord("z"):
#         print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end='')
#     else:
#         print(p,end='')


# 【例3-5】谁在说谎
# 编写程序，解决以下问题。
# 4个人中有一人做了好事，已知有三个人说了真话，根据下面对话判断是谁做的好事。
# A说：不是我；
# B说：是C；
# C说：是D；
# D说：C胡说
# for name in ['A','B','C','D']:
#     if(name!='A')+(name=='C')+(name=='D')+(name!='D')==3:
#         print(name,"做了好事！")

# 【例3-6】计次
# time =8
# while time<12:
#     print("time={},有效次数内".format(time))
#     time+=1
# else:
#     print("计数完毕")


# 【例3-7】计算π的近似值
# number=1
# i=1
# count=3
# flag=-1
# while abs(i) >10**(-6):
#     i=1/count
#     i=flag*i
#     number=i+number
#     flag = flag*-1
#     count += 2
#     print(i)
# print("近似值是：{}".format(number))


# 【例3-8】九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         print("{}*{}={}".format(i,j,i*j))


# 【例3-9】三角形图案
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end="")
#     print("\n")

# 【例3-10】：打10次游戏
# import random
#
# game=10
# for i in range(10):
#     print("正在打第{}场游戏".format(i+1))
#     feeling=random.randint(1,10)
#     if(5<feeling<10):
#         print("不想玩了，下一把！")
#         continue
#     if(feeling==10):
#         print("好气,今天不打了")
#         break
#     else:
#         print("开心")
#     result=random.randint(0,1)
#     if(result==1):
#         print("朋友圈炫耀")
#     else:
#         print(".....QAQ")


# 【例3-15】猜颜色
# 编写程序，随机产生色子的一面（数字1～6），给用户三次猜测机会，程序给出猜测提示（偏大或偏小）。如果某次猜测正确，则提示正确并中断循环；如果三次均猜错，则提示机会用完
# import random
# i=3
# touzi=random.randint(1,6)
# while i>0:
#     usernumbei = eval(input("请输入你的猜测："))
#     if(usernumbei==touzi):
#         print("恭喜猜中！")
#         break
#     if(usernumbei>touzi):
#         print("您猜的大了")
#         i=i-1
#     else:
#         print("您猜的小了")
#         i=i-1


# 【例3-16】
# 编写程序，从键盘输入一段文字，如果其中包括“密”字（可能出现0次、1次或者多次），则输出时过滤掉该字，其他内容原样输出
# sentence=input("请输入文字：")
# for letter in sentence:
#     if(letter=="密"):
#         continue
#     else:
#         print(letter,end='')


# 【例3-17】
# 编写程序，从键盘输入密码，如果密码长度小于6，则要求重新输入。如果长度等于6，则判断密码是否正确，如果正确则中断循环，否则提示错误并要求继续输入。
reflectword="123456789"
while 1:
    password = input("请输入密码：")
    if(len(password)<6):
        print("密码长度错误，请重新输入")
        continue
    if(password==reflectword):
        print("恭喜，密码正确")
        break
    else:
        print("密码错误,请重新输入：")
        continue