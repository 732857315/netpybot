import requests
import api_mode_openai
import urllib.parse  # 导入包

def keyword(message, uid, gid=None):
    #if message == '来张色图':
    #    setu(uid, gid)
    test(message, uid, gid)
 
def test(message, uid, gid):
##    if gid == 960836183: # 自己测试
##        #put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
##        #requests.get(url=put.format(gid, '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)))
##        if message[0:9] == '/chatGPT ': # if uid == 1521746863
##            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
##            msg = '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)+' :'
##            msgopenai = api_mode_openai.api_openai_chatgpt3turbo(message[9:])
##            requests.get(url=put.format(gid, msg + urllib.parse.quote(msgopenai,encoding="utf-8") ) )
##            #print(msgopenai)
    if "[CQ:at,qq=195891736]" in message:
        put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
        msg = '[CQ:at,qq='+str(uid)+']'+'我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】，有任何问题联系QQ:732857315，当前openai'+api_mode_openai.api_openai_credit_grants()+' '
        requests.get(url=put.format(gid, msg) )
    if (gid == 118991356)or(gid == 960836183)or(gid == 808033307)or(gid == 755402727)or(gid == 601642297):
        if message == "/测试机器人对话": # if uid == 1521746863
            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            requests.get(url=put.format(gid, '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)))
        if message[0:9] == '/chatGPT ':
            if 1:#((uid==732857315)or(uid==1521746863)or(uid==3325798716)): # if uid == 1521746863
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                msg = '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)+' :测试用途，请联系732857315，以后会开源 '+api_mode_openai.api_openai_credit_grants()+' '
                msgopenai = api_mode_openai.api_openai_chatgpt3turbo(message[9:])
                requests.get(url=put.format(gid, msg + urllib.parse.quote(msgopenai,encoding="utf-8") ) )
                #print(msgopenai)
            else:
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                msg = '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)+' :'
                msgopenai = 'QQ未添加，请联系732857315，测试用途，以后会开源'
                requests.get(url=put.format(gid, msg + msgopenai) )

    elif gid==None:
        put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
        msg = '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】，有任何问题联系QQ:732857315，当前openai'+api_mode_openai.api_openai_credit_grants()+' '
        requests.get(url=put.format(uid, msg))
    
def setu(uid, gid=None):
    num = 20
    url = 'https://api.lolicon.app/setu'
    params = {'r18': 1,
              'size1200': True,
              'num': num}
    menu = requests.get(url, params=params)
    # print(menu.json()['data'][0]['urls']['original'])
    for i in range(num):
        print(menu.json()['data'][i]['url'])
        setu_url = menu.json()['data'][i]['url']  # 对传回来的网址进行数据提取
 
        if gid:
            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(gid, pic_path))
            requests.get(url=put.format(gid, '已经发了一张图，没看到就是被吞了'))
        else:
            print(uid)
            put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
            pic_path = r'[CQ:image,' r'file=' + setu_url + r']'
            print(pic_path)
            requests.get(url=put.format(uid, pic_path))
        
