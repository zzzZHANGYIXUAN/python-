# 编写程序，开发一个循环5次计算的小游戏，每次随机产生两个100以内的数字，让用户计算两个数字之和并输入结果，如果计算结果正确则加一分，如果计算结果错误则不加分。如果正确率大于等于80%，则闯关成功
import random
score=0
i=5
while(i!=0):
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    print("本次产生的数字为：" + str(number1) + "," + str(number2))
    sum = float(input("请输入您计算的结果："))
    if (sum == number1 + number2):
        score = score + 1
    i = i - 1
if(score>=4):
    print("恭喜，闯关成功！")
else:
    print("加油，再接再厉！")
