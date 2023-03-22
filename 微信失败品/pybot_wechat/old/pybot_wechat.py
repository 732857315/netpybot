
import json
import requests
import threading
import sys,os
import time

import pybot_wechat_rgb
from lxml import etree

def Log(msg,mode = 'ERROR'):
    if mode == 'ERROR':
        print(mode+' Message: '+msg+' ,File: "' + __file__ + '", Line ' + str(sys._getframe().f_lineno) ) #+ #' , in ' +   sys._getframe().f_code.co_name)
    elif mode == 'LOG':
        print(mode+' Message: '+msg+' ,File: "' + __file__ + '", Line ' + str(sys._getframe().f_lineno) )#+ #' , in ' +   sys._getframe().f_code.co_name)
              
# 1获取uuid  用于获取显示二维码以及登录

##t = time.time()
##t = int(t)
#4096*24*3600
try:
    url = 'https://login.wx.qq.com/jslogin'
    params = {
        'appid':'wx782c26e4c19acffb', # wxeb7ec651dd0aefa9    早期：wx782c26e4c19acffb
        'fun':'new',
        'lang':'zh_CN',
        'Accept-Encoding':'gzip, deflate, br'
        }

    request = requests.post(url,params=params)
    #print(start.headers)
    #print(request.text) 

    requesttext = json.loads('{\"'+request.text.replace(';',',\"',1).replace('=','\":',2).replace(';','').replace(' ','')+'}')
    #print(requesttext)
    #print(requesttext.get('window.QRLogin.uuid'))
    wechat_uuid = requesttext.get('window.QRLogin.uuid')
except:
    print('pybot_wechat get uuid ERROR!')
# 2获取二维码  用于显示二维码以及登录
try:
    url = 'https://login.weixin.qq.com/qrcode/'+wechat_uuid
    params = {
        't':''
        }
    request = requests.get(url,params=params)
    request.encoding = 'unicode_escape'
    qcfile=request.content

    #print(qcfile)
    QCimage_path = './QCwechat.jfif'
    QCtxt_path = './QCwechat.txt'
    f_qc = open(QCimage_path, mode = 'wb') #,encoding ='unicode_escape'
    try:
        f_qc.write(qcfile)
    finally:
        f_qc.close()

    pybot_wechat_rgb.process_image(QCimage_path,QCtxt_path) #控制台显示二维码
    print('控制台微信扫描上方二维码登陆')
except:
    print('pybot_wechat get qc ERROR!')
# 3轮询二维码登陆状态
try:
    url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'
    params = {
        'tip':1,
        'uuid':wechat_uuid
        }
    number_connect=0
    max_connect = 3
    max_delaytim= 30
    start = 0
    while True:
        number_connect += 1;
        if start==1:
            print('剩余确认时间:'+str(max_delaytim+max_connect-number_connect))
        elif number_connect==max_connect:
            print('connect_num:'+str(number_connect)+' 即将关闭')
        else:
            print('connect_num:'+str(number_connect))
        request = requests.get(url,params=params)
        if ('window.redirect_uri' in request.text):
            #print(request.text[request.text.index('window.redirect_uri=')+21:request.text.rindex(';')-1])
            break
        requesttext = json.loads('{\"'+request.text.replace('=','\":',2).replace(';','').replace(' ','')+'}')
        #print(requesttext)

        if requesttext.get('window.code') == 408:
            print('登陆超时')
            if number_connect>=max_connect : #尝试次数 3
                break
            continue
##        elif requesttext.get('window.code') == 200:
##            print('确认登陆')
##            break
        elif requesttext.get('window.code') == 201:
            if start==0:
                print('扫描成功')
                start=1
            time.sleep(1);
            if number_connect>=max_delaytim+max_connect: #尝试次数 扫描后等待确认时间 10+3  - 3 =  10s
                break
            continue
        else:
            Log('pybot_wechat qc ERROR!')
            break
except:
    print('pybot_wechat qc ERROR!')
# 4登录并获取公参
uos_patch_extspam = 'Go8FCIkFEokFCggwMDAwMDAwMRAGGvAESySibk50w5Wb3uTl2c2h64jVVrV7gNs06GFlWpl\
HQbY/5FfiO++1yH4ykCyNPWKXmco+wfQzK5R98D3so7rJ5LmGFvBLjGceleySrc3SOf2Pc1gVehzJgODeS0lDL3/I/\
0S2SSE98YgKleq6Uqx6ndTy9yaL9qFxJL7eiA/R3SEfTaW1SBoSITIu+EEkXff+Pv8NHOk7N57rcGk1w0ZzRrQDkXT\
OXFN2iHYIzAAZPIOY45Lsh+A4slpgnDiaOvRtlQYCt97nmPLuTipOJ8Qc5pM7ZsOsAPPrCQL7nK0I7aPrFDF0q4ziU\
UKettzW8MrAaiVfmbD1/VkmLNVqqZVvBCtRblXb5FHmtS8FxnqCzYP4WFvz3T0TcrOqwLX1M/DQvcHaGGw0B0y4bZM\
s7lVScGBFxMj3vbFi2SRKbKhaitxHfYHAOAa0X7/MSS0RNAjdwoyGHeOepXOKY+h3iHeqCvgOH6LOifdHf/1aaZNwS\
kGotYnYScW8Yx63LnSwba7+hESrtPa/huRmB9KWvMCKbDThL/nne14hnL277EDCSocPu3rOSYjuB9gKSOdVmWsj9Dx\
b/iZIe+S6AiG29Esm+/eUacSba0k8wn5HhHg9d4tIcixrxveflc8vi2/wNQGVFNsGO6tB5WF0xf/plngOvQ1/ivGV/\
C1Qpdhzznh0ExAVJ6dwzNg7qIEBaw+BzTJTUuRcPk92Sn6QDn2Pu3mpONaEumacjW4w6ipPnPw+g2TfywJjeEcpSZa\
P4Q3YV5HG8D6UjWA4GSkBKculWpdCMadx0usMomsSS/74QgpYqcPkmamB4nVv1JxczYITIqItIKjD35IGKAUwAA=='
#try:
url = request.text[request.text.index('window.redirect_uri=')+21:request.text.rindex(';')-1]
url = url.replace('https://wx.qq.com','https://wx.qq.com?target=t',1)
headers = {
    'client-version' :'2.0.0',
    'extspam':uos_patch_extspam #uos绕过无法登陆
    }
params = {
    'fun':'new',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
request = requests.get(url,headers=headers,params=params)
print(request.cookies)
print(request.headers)
print(request.text)

print(str(request.text.find('wxsid')))
##params = {
##    'fun':'new',
##    'Cookie':request.headers.get('Set-Cookie'),
##    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
##    }
##request = requests.get(url,headers=headers,params=params)
##print(request.cookies)
##print(request.headers)
##
##params = {
##    'fun':'new',
##    'Cookie':request.headers.get('Set-Cookie'),
##    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
##    }
##request = requests.get(url,headers=headers,params=params)
##print(request.cookies)
##print(request.headers)

##html = etree.HTML(request.text)
###wxsid = html.xpath(u"//wxsid")[0]
##print(html)

#print(wxsid.text.strip())
#参数示例
##    {
##    'Connection': 'keep-alive',
##    'Content-Type': 'text/html; charset=utf-8',
##    'Cache-Control': 'no-cache, must-revalidate',
##    'Set-Cookie': 'mm_lang=zh_CN; Domain=wx.qq.com; Path=/; Expires=Tue, 07-Mar-2023 03:47:19 GMT; Secure',
##    'Strict-Transport-Security': 'max-age=31536000',
##    'Content-Encoding': 'gzip',
##    'Content-Length': '19327'
##    }
#except:
#    print('pybot_wechat login ERROR!')
    
print('end')
###window.code=xxx;
##xxx:
##408 登陆超时
##201 扫描成功
##200 确认登录
##当返回200时，还会有如下内容
##window.redirect_uri="x";

##
##url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login'
##params = {
##    'loginicon':'true',
##    'uuid':requesttext.get('window.QRLogin.uuid'),
##    'tip'=0,
##    'r'=t-4096*24*3600
##    #_=1678014738387
##    }
##
##request = requests.get(url,params=params)
##
##print(request.text)
