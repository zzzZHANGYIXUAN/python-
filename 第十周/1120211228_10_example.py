# 遍历所有的键-值对
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# print("dice:{},len:{}".format(student_dict,len(student_dict)))
# for k,v in student_dict.items():
#     print("k:{},v:{}".format(k,v))
# for item in student_dict.items():
#     print("k:{},v:{}".format(item[0],item[1]))
#     print(item)



# 遍历字典中的所有键
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# print("dice:{},len:{}".format(student_dict,len(student_dict)))
# for k in student_dict.keys():
#     print("k:{}".format(k))
# for k in student_dict:
#     print("k:{}".format(k))


# 遍历字典中的所有值
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# print("dice:{},len:{}".format(student_dict,len(student_dict)))
# for v in student_dict.values():
#     print("v:{}".format(v))


# 操作组合数据11：修改
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# student_dict['101']="老马"
# print(student_dict)


# 操作组合数据12：增加
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# student_dict['104']='老马'
# print(student_dict)


# 操作组合数据13：删除
# student_dict={"101":"彭一","102":"李二","103":"张三"}
# student_dict.pop('101')
# print(student_dict)



# <file>.read()【例10-1】
# 读入全部文本内容，返回结果为一个字符串
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# content=f1.read()
# print(content)
# f1.close()


# <file>.readline() 【例10-2】
#读入一行文本内容，返回结果为一个字符串
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# content=f1.readline()
# print(content)
# f1.close()


# <file>.readlines() 【例10-3】
# 读入全部文本内容，返回结果为一个列表
# 列表中的每个元素为一行文本字符串
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# content=f1.readlines()
# print(content)
# f1.close()


# for循环+文件【例10-4】
# 每次循环读取文件的一行
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# for line in f1.readlines():
#     print(line)
# f1.close()



# 处理每行内容【例10-6】
# 去除每行首尾的空格/换行符
# <str>.strip()
# <str>.lstrip()
# <str>.rstrip()
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# for line in f1.readlines():
#     newline=line.strip()
#     print(newline)
#     print(line)
# f1.close()


# 处理每行内容【例10-7】
# 根据分隔符进行分割，返回值为列表
# <str>.split(<分隔符>)
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# for line in f1.readlines():
#     newwords=line.split(" ")
#     print(newwords)
# f1.close()



# student_dict={"101":"彭一","102":"李二","103":"张三"}
# itmes=list(student_dict.items())
# print(itmes)
# 词频统计代码实现【例10-11】
#关键步骤1：处理符号以及大小写。
# 关键步骤2：如何统计
# 关键步骤3：频率有高到低排列
# path="F:/lemontree.txt"
# f1=open(path,'r',encoding="utf-8")
# content=f1.read()
# #把文本内容读取到字符串content中
# content=content.lower()
# #把所有字母改为小写
# for ch in [',',':','.']:
#     content = content.replace(ch,' ')
# #用空格替换， ： 。
# words = content.split()
# #把内容分割为列表words
# counts = {}
# #计数的字典counts
# for word in words:
#     if(len(word)==1):
#         continue
#     else:
#         counts[word]=counts.get(word,0)+1
# #排序
# itmes=list(counts.items())
# #把字典转化为列表
# itmes.sort(key=lambda x:x[1],reverse=True)
# #按照元素的第2列(第1列的序列号是0)排序，降序
# for i in range(10):
#     word,count = itmes[i]
#     print("{}=={}".format(word,count))
# #输出排序前十的词语



# # 【例10-12】
# import jieba
# ret=jieba.lcut("北京人是从北京人进化来的")
# print(ret)


# 《三国演义》中文词频统计【例10-13】
# import jieba
# path="F:/三国演义.txt"
# f1=open(path,'r',encoding="utf-8")
# content=f1.read()
# #把文本内容读取到字符串content中
# words = jieba.lcut(content)
# #把内容分割为列表words
# counts = {}
# #计数的字典counts
# for word in words:
#     if(len(word)==1):
#         continue
#     else:
#         counts[word]=counts.get(word,0)+1
# #排序
# itmes=list(counts.items())
# #把字典转化为列表
# itmes.sort(key=lambda x:x[1],reverse=True)
# #按照元素的第2列(第1列的序列号是0)排序，降序
# for i in range(25):
#     word,count = itmes[i]
#     print("{}=={}".format(word,count))
# #输出排序前25的词语


