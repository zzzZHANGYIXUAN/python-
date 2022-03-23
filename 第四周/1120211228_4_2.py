#BMI值计算,分别输入身高和体重，输出BMI值，并保留1位小数
hight=float(input("请输入身高，单位米："))
weight=int(input("请输入体重，单位公斤："))
bmi=weight/(hight*hight)
print("你的bmi是："+"{:.1f}".format(bmi))
