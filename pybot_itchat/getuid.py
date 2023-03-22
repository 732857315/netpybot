
import hashlib

import hashlib

# 假设这是原始数据
data = "@@w732857315"
yuanmiwen='3eabc3c12019b3164bff1e4f755ae00917515079b2d5f658085d43efdbeec2a3'
# 计算两个 SHA256 校验和
hash1 = hashlib.sha256(data.encode()).hexdigest()
hash2 = hashlib.sha256(data.encode()).hexdigest()
print(hash1)
print(hash2)
# 判断两个校验和是否相等
if hash1 == hash2:
    print("两个校验和相等")
else:
    print("两个校验和不相等")
