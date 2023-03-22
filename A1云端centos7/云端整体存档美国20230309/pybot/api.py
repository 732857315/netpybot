import requests
import api_mode_openai
import urllib.parse  # 导入包

def keyword(message, uid, gid=None):
    #if message == '来张色图':
    #    setu(uid, gid)
    test(message, uid, gid)

Master_gid_list = [
        118991356, #测试群 
        960836183, #小号群
        808033307, #FPGA群 人多 2000
        755402727, #考研交流群 人少 20
        601642297, #舍群  人少 10
        1157797199 #配音  人少 170
    ]
Master_uid_list = [
        732857315,
        
    ]
def test(message, uid, gid):
    ## 私聊信息
    if gid==None:
        #最高级管理员
        if uid in Master_uid_list:
            print('管理员私聊信息')
        ## 固定消息
        if "/测试机器人对话" == message.replace(' ',''):
            put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
            requests.get(url=put.format(uid, '私聊消息 QQ:'+str(uid)))
            print(url)
            return
        ## 变长消息
        if (message[0:9] == '/chatGPT '):
            put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
            msg = '@'+str(uid)+' '+'机器人目前测试用途，请联系732857315，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
            msgopenai = api_mode_openai.api_openai_chatgpt3turbo(message[9:])
            try:
                msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
            except:
                msgopenai = str(msgopenai)
            requests.get(url=put.format(uid, msg + msgopenai ) )
            print(url)
            return
        put = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}&auto_escape=false'
        msg = '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】群聊中还可以【@我 你的对话】，有任何问题联系QQ:732857315，当前openai'+api_mode_openai.api_openai_credit_grants()+' '
        requests.get(url=put.format(uid, msg))
        print(url)
        
    ## 群聊信息
    else:
        #最高级管理员
        if uid in Master_uid_list:
            print('管理员群聊信息')
        ## 特权群聊
        if gid in Master_gid_list:#判断是否在特权群列表
            ## 固定消息
            if ("[CQ:at,qq=195891736]" == message.replace(' ','')):
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                msg = '[CQ:at,qq='+str(uid)+'] ' + '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】或者直接【@我 你的对话】，有任何问题联系QQ:732857315，当前openai' + api_mode_openai.api_openai_credit_grants()
                requests.get(url=put.format(gid, msg) )
                print(url)
                return
            ## 固定消息
            if "/测试机器人对话" == message.replace(' ',''):
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                requests.get(url=put.format(gid, '群聊消息 QQ群:'+str(gid)+' QQ:'+str(uid)))
                print(url)
                return
            ## 变长消息
            if (message[0:9] == '/chatGPT '):
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                msg = '[CQ:at,qq='+str(uid)+'] '+'机器人目前测试用途，请联系732857315，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
                msgopenai = api_mode_openai.api_openai_chatgpt3turbo(message[9:])
                try:
                    msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
                except:
                    msgopenai = str(msgopenai)
                requests.get(url=put.format(gid, msg +  msgopenai) ) 
                print(url)
                return
            ## 变长消息
            if (message[0:20] == '[CQ:at,qq=195891736]'):
                put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
                msg = '[CQ:at,qq='+str(uid)+'] '+'机器人目前测试用途，请联系732857315，以后会开源 ' + api_mode_openai.api_openai_credit_grants() + ' : '
                msgopenai = api_mode_openai.api_openai_chatgpt3turbo(message[20:])
                try:
                    msgopenai = urllib.parse.quote(msgopenai,encoding="utf-8")
                except:
                    msgopenai = str(msgopenai)
                requests.get(url=put.format(gid, msg +  msgopenai) ) 
                print(url)
                return
        ## 非特权
        ## 固定消息
        if ("[CQ:at,qq=195891736]" == message.replace(' ','')):
            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            msg = '[CQ:at,qq='+str(uid)+'] ' + '我是一个正在测试状态的机器人，当前命令有【/测试机器人对话】【/chatGPT 你的对话】或者直接【@我 你的对话】，本群是非特权无法使用命令【/chatGPT 你的对话】或者直接【@我 你的对话】，有任何问题联系QQ:732857315，当前openai' + api_mode_openai.api_openai_credit_grants()
            requests.get(url=put.format(gid, msg) )
            print(url)
            return
        ## 固定消息
        if "/测试机器人对话" == message.replace(' ',''):
            put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
            requests.get(url=put.format(gid, '非特权无法使用命令【/chatGPT 你的对话】或者直接【@我 你的对话】 QQ群:'+str(gid)+' QQ:'+str(uid)))
            print(url)
            return

            
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
        

