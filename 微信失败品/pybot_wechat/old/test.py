

import json
d='window.code=200;\nwindow.redirect_uri=\"https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=AX7d0RdH8mRnnzSBM6JTPPAJ@qrticket_0&uuid=IdW8SDot1w==&lang=zh_CN&scan=1678111906\";'
d=str(d)
d=d[d.index('window.redirect_uri=')+21:d.rindex(';')-1] #
d={'Connection': 'keep-alive', 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-cache, must-revalidate', 'Set-Cookie': 'mm_lang=zh_CN; Domain=wx.qq.com; Path=/; Expires=Tue, 07-Mar-2023 04:23:20 GMT; Secure', 'Strict-Transport-Security': 'max-age=31536000', 'Content-Encoding': 'gzip', 'Content-Length': '19327'}


print(d.get('Set-Cookie'))

