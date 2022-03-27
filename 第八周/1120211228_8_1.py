# 利用python的print()函数写一篇作文
# 要求必须覆盖以下列表操作
rewad1_name=['张三', '李四', '王五']
rewad2_name=['刘大', '马二', '程六', '何七']
rewad3_name=['钱八', '元九', '项十', '孙十一', '周十二']
print("女士们，先生们，欢迎来到谁是幸运儿。我是节目主持人XUAN，我来为大家公布我们的获奖名单！")
print("我们的一等奖获得者一共{}位，他们是{}".format(len(rewad1_name),",".join(rewad1_name)))
print("我们的二等奖获得者一共{}位，他们是{}".format(len(rewad2_name),",".join(rewad1_name)))
print("我们的三等奖获得者一共{}位，他们是{}".format(len(rewad3_name),",".join(rewad1_name)))
rewad_name=rewad1_name+rewad2_name+rewad3_name
print("本期节目的获奖者共计{}位，他们是{}！".format(len(rewad_name),rewad_name))
print("让我们为一等奖的获得者欢呼吧{}".format(",".join(rewad1_name*2)))
print("第一位获奖者是：{},最后一位获奖者是：{}".format(rewad_name[0],rewad_name[-1]))
print("现场有观众赖子要求查询他是否再获奖名单中，我们一起看一下！")
jugment='赖子' in rewad_name
if jugment==0:
    print("没有他的名字！")
else:
    print("节目组忘记了")
print("让我们看一下年龄最大的获奖者和年龄最小的获奖者，他们是{}和{}".format(max(rewad_name),min(rewad_name)))
print("让我们看一下，获奖者中一共有几位叫做张三的朋友")
print("有{}位姓张的朋友".format(rewad_name.count('张三')))
print("刚才后台导演通知我们，赖子是在获奖者名单中，我们把他加上去！")
rewad_name.append("赖子")
print("同时，张三先生让自己的儿子来领奖，我们把名字换为张小三")
rewad_name[0]="张小三"
print("最后，节目组宣布，经费有限，减少开支，最后一位朋友{}只能说抱歉了".format(rewad_name.pop()))
print("让我们的一共{}位获奖者按照年龄由小到大排队上来把{}".format(len(rewad_name),sorted(rewad_name)))

