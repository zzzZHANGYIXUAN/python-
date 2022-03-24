# 内部参数输入
# x=20
# y=4*x+5
# print(y)


# 随机数据输入
# import random
# x = random.randint(0,20)
# y=4*x+5
# print(y)


# 控制台输入
# x= eval(input("x:"))
# y=4*x+5
# print(y)


# type函数
# print(type(1))
# print(type(2.3))
# print(type("hello"))


# eval函数
# aaa=eval("123")
# bbb=eval("123.5")
# c=eval("asc")
# print(type(aaa))
# print(type(bbb))
# print(type(c))
# a=eval(input("请输入x："))
# print(type(a))

#坚持的力量


#索引访问
# greet="jiayou nuli"
# print(greet[1])
# print(greet[5])
# print(greet[3:])
# print(greet[:3])
# print(greet[0:6])

# 字符串操作示例
# weekstr="星期一星期二星期三星期四星期五星期六星期日"
# weekid=eval(input("请输入星期数组（1-7）："))
# pos=(weekid-1)*3
# print(weekstr[pos:pos+3])

# 将单个小写字母加密
# character=input("请输入明文：")
# password=chr(ord("a")+(ord(character)-ord("a")+3)%26)
# print("密码为：")
# print(password)

# format()方法
dollar=eval(input("请输入美元数量："))
rmb=dollar*6.868
print("换算为人民币：{:.2f}".format(rmb))
print("换算为人民币：{0:-^30}".format(rmb))
print("换算为人民币：{0: ^30}".format(rmb))
print("换算为人民币：{0:?^30}".format(rmb))
