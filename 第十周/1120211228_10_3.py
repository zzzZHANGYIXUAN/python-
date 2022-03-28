# 读入score.txt文件，统计每个年级的不及格人数]
# 挂科分数按照75为分界线
path="F:/score.txt"
f1=open(path,"r",encoding="utf-8")
fail={}
count=0
for line in f1.readlines():
    line=line.replace("\n","")
    list=line.split(" ")
    if count>0:
        if list[3] not in fail:
            fail[list[3]]=0
        else:
            if int(list[1])<75 or int(list[2])<75:
                fail[list[3]] = fail[list[3]]+1
    count = count + 1
for k,v in fail.items():
    print("{0}年级挂科有{1}人".format(k, v))