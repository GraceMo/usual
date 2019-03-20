import itchat
import time
print("请扫描二维码登陆微信:")
itchat.auto_login()
print("登陆成功")
user = input("输入好友昵称:")
users = itchat.search_friends(name=user)
print(users)
#[<User: {'City': '烟台', 'VerifyFlag': 0, 'RemarkPYQuanPin': 'xiaoliang', 'StarFriend': 1, 'ChatRoomId': 0, 'DisplayName': '', 'EncryChatRoomId': '', 'Sex': 1, 'OwnerUin': 0, 'MemberList': <ContactList: []>, 'Signature': '生活如果欺骗了你', 'AttrStatus': 33558629, 'Alias': '', 'UserName': '@52d7104158d3c3e108eefb1b6e81dbf2682e5593b268a289961289a4084262ce', 'ContactFlag': 67, 'SnsFlag': 1, 'MemberCount': 0, 'KeyWord': '', 'IsOwner': 0, 'UniFriend': 0, 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=681822988&username=@52d7104158d3c3e108eefb1b6e81dbf2682e5593b268a289961289a4084262ce&skey=@crypt_539f90d8_66a6fe7e518d57974ef0cb840e633780', 'Province': '山东', 'HideInputBarFlag': 0, 'Uin': 0, 'AppAccountFlag': 0, 'Statues': 0, 'NickName': '亮点', 'PYInitial': 'LD', 'RemarkName': '小亮', 'RemarkPYInitial': 'XL', 'PYQuanPin': 'liangdian'}>]
realname = users[0]["UserName"]

index = 0
while True:
    itchat.send(str(index),toUserName=realname)
    index += 1
    time.sleep(1)
