
import requests

access_token = ''
url = f"http://127.0.0.1:5700/send_private_msg?access_token={access_token}"
msg = "测试单向发送."
data={
    "user_id": "732857315",
    "message": msg
}
requests.post(url, data, timeout=5)
