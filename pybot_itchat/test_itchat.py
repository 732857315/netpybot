
import sys,os
import importlib
import itchat, time
from itchat.content import *
import json

from multiprocessing import Process

currentDir = os.getcwd()
os.chdir('../pybot/') # .. to go back one dir | you can do "../aFolderYouWant"
sys.path.insert(0, os.getcwd())

api_mode_openai = importlib.import_module("api_mode_openai")

os.chdir(currentDir) # to go back to your home directory



def logincall():
    usehelpMsg = "Bot 登陆成功！"
    itchat.send(usehelpMsg,toUserName="filehelper")
    print('finish login')
def exitcall():
    print('exit')


global masterusermay
global masteruser
global modemast
global timeold
masterusermay=''
masteruser=''
modemast=0
timeold=0


##@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
##def text_reply(msg):
##    msg.user.send('%s: %s' % (msg.type, msg.text))
##    
##
##@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
##def download_files(msg):
##    msg.download(msg.fileName)
##    typeSymbol = {
##        PICTURE: 'img',
##        VIDEO: 'vid', }.get(msg.type, 'fil')
##    return '@%s@%s' % (typeSymbol, msg.fileName)
##
@itchat.msg_register(FRIENDS) #新好友
# 收到好友邀请自动添加好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
        xxd = '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】群聊中还可以【@我 你的对话】，有任何问题联系QQ: 732857315 或者发邮件到 732857315@qq@com '
    itchat.send_msg(xxd, msg['RecommendInfo']['UserName'])
    #msg.user.verify()
    #msg.user.send(xxd)

@itchat.msg_register(TEXT, isGroupChat=True) #群聊逻辑
def text_reply(msg):
    print('群 '+msg['ToUserName']+' 用户 '+msg.actualNickName+'： '+msg.text)
    if(str(msg.text)=='/测试机器人对话'):
        xxd = (u'@'+msg.actualNickName+'\u2005'+' 群聊消息order测试ok')
        msg.user.send(xxd)
        print(xxd)
        return
    if msg.isAt:
        if(str(msg.text).replace(' ','')=='@netpybot'):
            xxd = '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】还可以【@我 你的对话】，有任何问题联系QQ:732857315 或者发邮件到 732857315@qq.com ，当前openai'+api_mode_openai.api_openai_credit_grants()+' '
            msg.user.send(xxd)
            return
        xxd = u'@'+msg.actualNickName+'\u2005'+'机器人目前测试用途，请联系732857315 或者发邮件到 732857315@qq@com ，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
        msgopenai = api_mode_openai.api_openai_chatgpt3turbo(str(msg.text).replace('@netpybot ','',1))
        try:
            msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
        except:
            msgopenai = str(msgopenai)
        msg.user.send(xxd+msgopenai)
        print(xxd+msgopenai)
        return
    if (str(msg.text)[0:9] == '/chatGPT '):
        xxd = u'@'+msg.actualNickName+'\u2005'+'机器人目前测试用途，请联系 732857315 或者发邮件到 732857315@qq@com ，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
        msgopenai = api_mode_openai.api_openai_chatgpt3turbo(str(msg.text)[9:])
        try:
            msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
        except:
            msgopenai = str(msgopenai)
        msg.user.send(xxd+msgopenai)
        print(xxd+msgopenai)
        return
    
##
#### 

####        proc = Process(target=process1, args=(msg))
##        proc.start()  
######if __name__ == "__main__": 

##proc.start()  
###proc.join()
@itchat.msg_register([TEXT]) #私聊逻辑 #unicode-escape  json.dumps()  json.loads()
def text_reply(msg):
    global masterusermay
    global masteruser
    global modemast
    global timeold
    if msg.type == 'Text':
        #print(itchat.search_friends(wechatAccount='w732857315'))
        print(msg['FromUserName']+': '+ str(msg.text))
        if (time.time()-timeold)>20:
            modemast==0
            masterusermay=''
            timeold=0
            print('/MASTER登陆超时')
            
        if modemast==0:
            if(str(msg.text)=='/MASTER'):
                msg.user.send(u'MASTER 登陆，请在接下来输入密码！')
                masterusermay=str(msg['FromUserName'])
                modemast=1;
                timeold = time.time()
                print('/MASTER登陆: %s'%(masterusermay))
                return
        if modemast==1:
            if(str(msg.text)=='wxc7586637039')and(masterusermay==str(msg['FromUserName'])):
                msg.user.send(u'欢迎MASTER:'+masterusermay)
                masteruser = masterusermay
                print('/MASTER %s 登陆成功'%(masterusermay))
                modemast=0
                masterusermay=''
                timeold=0
                
                return
            elif(masterusermay==str(msg['FromUserName'])):
                msg.user.send(u'用户登陆失败！')
                print('用户 %s 登陆成失败'%(masterusermay))
                modemast=0
                masterusermay=''
                timeold=0
                
                return
            
        if str(msg['FromUserName']) == masteruser: #"@83712596e01bf2d860bfc185fd0a8cf0c5f57f1cdb21acb352fcaacfc7a749c8"
            if(str(msg.text)==u'/关闭机器人'):
                msg.user.send(u'即将关闭,1s！')
                time.sleep(1)
                usehelpMsg = "Bot 退出！"
                itchat.send(usehelpMsg,toUserName="filehelper")
                msg.user.send(u'已关闭！')
                itchat.logout()
                return
        if(str(msg.text)==u'/测试机器人对话'):
            xxd = (str(msg['FromUserName'])+' 私聊消息order测试ok')
            msg.user.send(xxd)
            print(xxd)
            return
        if (str(msg.text)[0:9] == '/chatGPT '):
            xxd = u'机器人目前测试用途，请联系 732857315 或者发邮件到 732857315@qq.com ，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
            msgopenai = api_mode_openai.api_openai_chatgpt3turbo(str(msg.text)[9:])
            try:
                msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
            except:
                msgopenai = str(msgopenai)
            msg.user.send(xxd+msgopenai)
            print(xxd+msgopenai)
            return
        xxd ='我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】群聊中还可以【@我 你的对话】，有任何问题联系QQ: 732857315 或者发邮件到 732857315@qq.com '
        msg.user.send(xxd)
        print(xxd)


#
# 获取自己的用户信息，返回自己的属性字典
#itchat.search_friends()
# 获取特定UserName的用户信息
#itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
#itchat.search_friends(name='littlecodersh')
# 获取分别对应相应键值的用户
#itchat.search_friends(wechatAccount='littlecodersh')
# 三、四项功能可以一同使用
#itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')

##encoded_str = "3eabc3c12019b3164bff1e4f755ae00917515079b2d5f658085d43efdbeec2a3"
### 将16进制编码转换为二进制格式
##binary_str = bytes.fromhex(encoded_str)
### 使用base64进行解码
##decoded_str = base64.b64decode(binary_str)
### 打印解码后的字符串
##print(decoded_str.decode('utf-8'))
###需要base64

if __name__ == '__main__':
    itchat.auto_login(hotReload=False,enableCmdQR=2,\
                  loginCallback=logincall, exitCallback=exitcall)
    time.sleep(1)
    itchat.run()




