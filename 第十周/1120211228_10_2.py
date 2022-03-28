# 读入score.txt文件，统计每个年级的平均成绩
path="F:/score.txt"
f1=open(path,"r",encoding="utf-8")
#两个年级的专业课成绩
avg1={'2':0,'专业课1':0,'专业课2':0}
#第一个元素是计算年级人数的
avg2={'3':0,'专业课1':0,'专业课2':0}
count=0
#规避表头数据，并且计算平均成绩用的
for line in f1.readlines():
    line=line.replace("\n","")
    list=line.split(" ")
    if count>0:
        if list[3] in avg1:
            avg1['专业课1']=(int(avg1['专业课1'])*int(avg1['2'])+int(list[1]))/(int(avg1['2'])+1)
            avg1['专业课2']=(int(avg1['专业课2'])*int(avg1['2'])+int(list[2]))/(int(avg1['2'])+1)
            avg1['2'] += 1
        else:
            avg2['专业课1']=(int(avg2['专业课1'])*int(avg2['3'])+int(list[1]))/(int(avg2['3'])+1)
            avg2['专业课2']=(int(avg2['专业课2'])*int(avg2['3'])+int(list[2]))/(int(avg2['3'])+1)
            avg2['3'] += 1
    count = count + 1
avg1.pop("2")
avg2.pop("3")
for k,v in avg1.items():
    print("2年级专业课{0}均分为{1}".format(k, v))
for k, v in avg2.items():
        print("3年级专业课{0}均分为{1}".format(k, v))