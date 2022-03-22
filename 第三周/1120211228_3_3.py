#斐波那契数列的计算
a=b=sum=1
while(b<=10000):
    sum=sum+b
    a=b
    b=b+a
print("最大值小于等于10000的斐波那契数列之和为："+str(sum))