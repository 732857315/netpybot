
from flask import Flask,request
import api
import threading
import sys,os
import platform
import operator

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def post_data():
    '''监听函数：用于监听客户端的一切消息及事件，并将数据传给api.py来响应'''

    '''私信监听'''
    if request.get_json().get('message_type') == 'private':# 如果是私聊信息
        gid = None
        uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message') # 获取原始信息
        #api.keyword(message,uid)
        t1 = threading.Thread(target=api.keyword, args=(message,uid,gid))
        t1.start()
        print("私聊"+' QQ:'+str(uid)+':'+message)

    '''群聊信息监听'''
    if request.get_json().get('message_type') == 'group':# 如果是群聊信息
        gid = request.get_json().get('group_id') # 获取群号
        uid = request.get_json().get('sender').get('user_id') # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message') # 获取原始信息
        #api.keyword(message,uid,gid)
        t2 = threading.Thread(target=api.keyword, args=(message,uid,gid))
        t2.start()
        print("群聊"+' QQ群:'+str(gid)+' QQ:'+str(uid)+':'+message)

    '''入群监听——入群欢迎'''
    #if request.get_json().get('notice_type') == 'group_increase':
    #    gid = request.get_json().get('group_id')
    #    uid = request.get_json().get('user_id')
    #    message = None
    #    api.event(message,gid,uid)


    return 'OK'
def Init_all(seting=None):
    #os.system("ping baidu.com")
    currentDir = os.getcwd()
    os.chdir('../go-cqhttp/') # .. to go back one dir | you can do "../aFolderYouWant"
    sys.path.insert(0, os.getcwd())
    #部分需要的程序
    #systemname = platform.platform()
    systembits = platform.architecture()
    #print(os.getcwd())
    if (operator.eq(('64bit', 'WindowsPE'),systembits)):
        #os.startfile(os.getcwd()+'/go-cqhttp/go-cqhttp.exe')
        os.system('go-cqhttp.exe')
    elif (('64bit', 'ELF') == systembits ):
        #os.startfile(os.getcwd()+'/go-cqhttp/go-cqhttp')
        os.system('./go-cqhttp')
    else: #苹果('64bit', '')
        print("系统错误，可能是32位或苹果，未启动go-cqhttp注意！")
    
    os.chdir(currentDir) # to go back to your home directory
    
def app_http(seting=None):
    app.run(debug=False, host='127.0.0.1', port=5701)
    
if __name__ == '__main__':
    t3 = threading.Thread(target=Init_all, args=())
    t3.start()
#    app.run(debug=False, host='127.0.0.1', port=5701)
    t4 = threading.Thread(target=app_http, args=())
    t4.start()
#    os.system("ping " + post)
##    while True:
##        post_data()
