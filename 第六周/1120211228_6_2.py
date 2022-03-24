#闰年判断"
a=int(input("请输入年份："))
if(a%4==0 and a%100!=0):
    print('该年份是闰年')
elif(a%400==0):
    print('该年份是闰年')
else:
    print("该年份不是闰年")