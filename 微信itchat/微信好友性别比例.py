# coding:utf-8
import itchat

'''
微信好友性别比例,发送到手机文件助手
'''

itchat.login()

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算比例
total = len(friends[1:])
msg =  "好友总数:  %d\n男性好友：%.2f%%,%d\n女性好友：%.2f%%,%d\n未填性别：%.2f%%,%d" % (total,(float(male / total) * 100), male, float(female / total) * 100, female, float(other / total) * 100, other)
itchat.send_msg(msg, 'filehelper')
