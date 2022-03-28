# 读入score.txt文件，统计每个年级一共有多少人
path="F:/score.txt"
f1=open(path,"r",encoding="utf-8")
number={}
avg={}
fail={}
count=0
for line in f1.readlines():
    line=line.replace("\n","")
    list=line.split(" ")
    if count>0:
        if list[3] not in number:
            number[list[3]]=1
        else:
            number[list[3]] = number[list[3]]+1
    count = count + 1
for k,v in number.items():
    print("{0}年级共有{1}人".format(k, v))
#content是字符串类型，带着换行符号的
# str=""
# for line in f1.readlines():
#     str=str+line
# list=str.split(' ' or '\n')
# print(list)
#去除数据中的换行符号和表头,并且把每个数据作为一个元素添加到
