import itchat
from threading import Thread
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib



#微信接收，解密函数
@itchat.msg_register(itchat.content.TEXT)
def recv(msg):
    if id == msg['FromUserName']:
        c = msg.text
        d = decrypt(c,key)
        print('》》》',d)


def run():
    itchat.run()


#消息处理函数
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text,key):
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密后函数
def decrypt(c,key):
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(c))
    return bytes.decode(plain_text).rstrip('\0')    

#发送函数
def send():
    while 1:
        text = input('《《《')
        e = encrypt(text,key)  # 加密
        msg =  str(e.decode())
        itchat.send(msg,id)
       

def main():
    global meg
    global key
    global id
    print('   请扫码登陆微信   ')
    itchat.auto_login()
    print('本程序用于微信自动加解密发送')
    print('      design by kayak        ')
    print('')
    print('#####################################################################')
    print('《《《为可发送状态')
    print('》》》表示好友消息')
    print('#####################################################################')
    print('')
    print('以下请正确输入与好友约定的密钥')
    print('该密钥几乎可以是任意定长的字符串！（例如一段文字，甚至可以是一整本书的文字）,建议密码尽可能长')
    a = input('请输入该密钥：').encode("utf8")
    for i in range(60):
                print('                          >>>>>>><<<<<<<<                                     ')
    
    #两次sha2加密生成key
    b = hashlib.sha256(a).hexdigest()
    c = hashlib.sha256(b.encode("utf8")).hexdigest()
    key = c[6:38].encode('utf8')
    while True:
        try:
            friend = input('请输入好友昵称：')
            info = itchat.search_friends(nickName=friend)
            id = info[0]['UserName']
            t1 = Thread(target=send)
            ts = Thread(target=run)
            t1.start()
            ts.start()
         except:
            print('昵称错误，请正确输入')

if __name__ == '__main__':
    main()
