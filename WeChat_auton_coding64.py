import itchat
from threading import Thread
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib


@itchat.msg_register(itchat.content.TEXT)
def recv(msg):
    if id == msg['FromUserName']:
        c = msg.text
        d = decrypt(c,key)
        print('》》》',d)


def run():
    itchat.run()

'''def pri():
    while 1:
        print("a")'''

'''def send_date():
  while True:
    text = input("<<")
    e = encrypt(text,key)
    st =  str(e.decode())
    udpsocket.sendto(st.encode(), (desip, desport))
udpsocket = None
desip = ""
desport = 0'''
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text,key):
    #key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)

    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(c,key):
    #key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(c))
    return bytes.decode(plain_text).rstrip('\0')    


def send():
    while 1:
        text = input('《《《')
        
            
        #print(type(text),text)
        e = encrypt(text,key)  # 加密
        #d = decrypt(text)  # 解密
        a =  str(e.decode())
        itchat.send(a,id)
        #print("已发送加密:",  a)


def main():
    global a
    global key
    global id
    print('   请扫码登陆微信   ')
    itchat.auto_login()
    print('本程序用于微信自动加解密发送')
    print('      design by kay         ')
    print('')
    print('#####################################################################')
    print('《《《为可发送状态')
    print('xxxxxx》》》《《《表示好友消息')
    print('#####################################################################')
    print('')
    print('以下请正确输入与好友约定的密钥')
    print('该密钥几乎可以是任意定长的字符串！（例如一段文字，甚至可以是一整本书的文字）,建议密码尽可能长')
    a = input('请输入该密钥：').encode("utf8")
    for i in range(60):
                print('                          >>>>>>><<<<<<<<                                     ')
    b = hashlib.sha256(a).hexdigest()
    c = hashlib.sha256(b.encode("utf8")).hexdigest()
    d = hashlib.sha256(c.encode("utf8")).hexdigest()
    key = d[6:38].encode('utf8')
    friend = input('请输入好友名称：')
    info = itchat.search_friends(nickName=friend)
    id = info[0]['UserName']
    print(id)
    t1 = Thread(target=send)
    ts = Thread(target=run)
    t1.start()
    ts.start()
main()
