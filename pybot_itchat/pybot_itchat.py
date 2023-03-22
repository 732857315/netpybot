
import time
import itchat
from itchat.content import *

@itchat.msg_register(TEXT)
def text_reply(msg):
    #msg.user.send('%s: %s' % (msg.type, msg.text))
    return '自动回复：{}'.format(msg.text)

##@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
##def download_files(msg):
##    msg.download(msg.fileName)
##    typeSymbol = {
##        PICTURE: 'img',
##        VIDEO: 'vid', }.get(msg.type, 'fil')
##    return '@%s@%s' % (typeSymbol, msg.fileName)

##@itchat.msg_register(FRIENDS)
##def add_friend(msg):
##    msg.user.verify()
##    msg.user.send('Nice to meet you!')

##@itchat.msg_register(TEXT, isGroupChat=True)
##def text_reply(msg):
##    if msg.isAt:
##        msg.user.send(u'@%s\u2005I received: %s' % (
##            msg.actualNickName, msg.text))

#通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码

itchat.auto_login(hotReload = True)
time.sleep(1)
if __name__ == '__main__':
    itchat.run()
    usehelpMsg = "Bot 登陆成功"
    itchat.send(usehelpMsg,toUserName="filehelper")

