# 1.序列的索引操作 【例4-1】
#字符串
# aaa="hello world"
# print(aaa[0])
# print(aaa[1])
# print(aaa[-1])
#元组
# b="宝马 奔驰 奥迪"
# print(b[0])
# print(b[1])
# print(b[-1])
#列表
# c=["高铁","飞机","汽车"]
# print(c[0])
# print(c[1])
# print(c[-1])


# 2.序列的切片操作 【例4-2】
# 字符串
# aaa="hello world"
# print(aaa[0:2])
# print(aaa[1:])
# print(aaa[:-1])
# 元组
# b="宝马 奔驰 奥迪"
# print(b[0:])
# print(b[:1])
# print(b[-6:-1])
#列表
# c=["高铁","飞机","汽车"]
# print(c[0:2])
# print(c[1:])
# print(c[:-1])


# 3.序列相加 【例4-3】
#字符串
# a1="hello"
# a2=" "
# a3="world"
# a_add=a1+a2+a3
# print(a_add)
#元组
# b1=('hello')
# b2=" "
# b3=('world')
# b_add=b1+b2+b3
# print(b_add)
#列表
# b1=['hello']
# b2=[' ']
# b3=['world']
# b_add=b1+b2+b3
# print(b_add)


# 4.序列乘法 【例4-4】
#字符串
# a="hello"
# a_multi=a*4
# print(a_multi)
#元组
# a=("aodi")
# a_multi=a*4
# print(a_multi)
#列表
# a=["hello"]
# a_multi=a*4
# print(a_multi)


# 5.成员资格【例4-5】
#字符串
# a="hello world"
# print('w' in a)
# if 'w' in a:
#     print('yes')
# else:
#     print('no')
#列表
# a=["hello world"]
# print('hello world' in a)
# if 'hello world' in a:
#     print('yes')
# else:
#     print('no')
#元组
# a=("hello world")
# print('h=' in a)
# if 'h=' in a:
#     print('yes')
# else:
#     print('no')


# 6.序列长度【例4-6】
#字符串
# a="hello world"
# print(len(a))
#列表
# a=["hello" ,"world"]
# print(len(a))
#元组
# a=("hello" ,"world")
# print(len(a))


# 7.序列最大值【例4-7】\
# 返回列表元素中的最大值
#字符串
# a="hello world"
# print(max(a))
# #列表
# a=["hello","world"]
# print(max(a))
# #元组
# a=("hello","world")
# print(max(a))



# 7.序列最小值【例4-7】 返回列表元素中的最小值
#字符串
# a="hello world"
# print(min(a))
# #列表
# a=["hello","world"]
# print(min(a))
# #元组
# a=("hello","world")
# print(min(a))


# 9.序列计数【例4-9】
#字符串
# a="hello world"
# a_count1=a.count('l')
# a_count2=a.count('ll')
# print(a_count1,a_count2)
# #列表
# a=["hello", "world","world"]
# a_count1=a.count('hello')
# a_count2=a.count('world')
# print(a_count1,a_count2)
# #元组
# a=(1,2,3,4,5,6,1,1,1,3,3,3,3)
# a_count1=a.count(1)
# a_count2=a.count(3)
# print(a_count1,a_count2)


# for + 列表【例4-10】
# friend_list=["马云","马化腾","王健林","刘强东"]
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))

# 修改列表元素【例4-11】
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# friend_list[-1]="许家印"
# #替换指定位置的元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))



# 在列表中添加元素【例4-12】
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# friend_list.append("许家印")
# #列表末尾添加元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))


# 在列表中添加元素(2) 【例4-13】
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# friend_list.insert(1,"许家印")
# #列表指定位置插入元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))



# # 从列表中删除元素【例4-14】
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# # del friend_list[-1]
# # #删除最后一个元素
# # for friend in friend_list:
# #     print("{},好哥们，谢谢你来给我过生日".format(friend))
# del friend_list[:-2]
# #删除到倒数第二个元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))



# 从列表中删除元素(2) 【例4-15】
# 使用方法pop()删除元素，并获得该元素
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# name1=friend_list.pop()
# print(name1)
# #默认删除最后一个元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# name2=friend_list.pop(2)
# print(name2)
# #删除指定位置元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))


# 从列表中删除元素(3) 【例4-16】
# friend_list=["马云","马化腾","王健林","刘强东"]
# print('--------2016年----------------------')
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))
# print('--------2017年----------------------')
# friend_list.remove('马云')
# #删除指定名称的元素
# for friend in friend_list:
#     print("{},好哥们，谢谢你来给我过生日".format(friend))


# 列表排序【例4-17】
# 使用方法sort()对列表进行永久性排序
# car=["bmw","audi","toyota","subaru"]
# car.sort()
# print(car)
# car.sort(reverse= True)
# print(car)



# 列表排序【例4-18】
# 使用函数sorted()对列表进行临时排序
#
# car=["bmw","audi","toyota","subaru"]
# print("原始列表为:{}".format(car))
# print("原始列表排序后为:{}".format(sorted(car)))
# print("再次输出原始列表为:{}".format(car))


# 反转列表【例4-19】
# 使用reverse()函数反转列表元素的排列顺序
# car=["bmw","audi","toyota","subaru"]
# print("原始列表为:{}".format(car))
# car.reverse()
# print("原始列表翻转排序后为:{}".format(car))
# print("再次输出原始列表为:{}".format(car))



# 一次input()获得多个值【例4-20】
# str.split(seq=None)
# 返回一个列表，由str根据sep被分割的部分构成
# student_names=input("请输入学术列表，用英文的逗号(,)分割:")
# print(student_names)
# student_list=student_names.split(",")
# print(student_list)


# 组合数据类型合并输出【例4-21】
# str.join(iterable)
# 返回一个新字符串，由组合数据类型iterable变量的每个元素组成，元素间用str分割
# friend_list=["马云","马化腾","王健林","刘强东"]
# sntence=",".join(friend_list)
# #把列表分割为了字符串，有英文的逗号来分割
# print(sntence)



# 例子：击鼓传花【例4-22】
import random
player=["大娃","二娃","三娃","四娃","五娃","六娃","七娃","孙悟空","哪吒","二郎神"]
print("参加的游戏的人数是：{}".format(len(player)))
print("参加游戏的人是:{}".format(",".join(player)))
player.sort()
print("请大家按照顺序坐好{}".format(",".join(player)))
del_number=0
while(len(player)>1):
    del_number=random.randint(0,len(player)-1)
    print("击鼓{}次，{}被淘汰了".format(del_number+1,player[del_number]))
    player.pop(del_number)
    print("留下的人数是{}，他们是{}".format(len(player),",".join(player)))
else:
    print("最后的幸存者是：{}".format(",".join(player)))

