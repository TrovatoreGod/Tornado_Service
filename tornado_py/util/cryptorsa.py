# -*- coding: UTF-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
import random


class rsacrypt():

    def __init__(self):
        self.random_generator = Random.new().read

    def key_pair(self):
        # random_generator = Random.new().read
        # rsa算法生成实例
        print(self.random_generator)
        rsa = RSA.generate(1024, self.random_generator)
        # master的秘钥对的生成
        public_pem = rsa.publickey().exportKey()
        private_pem = rsa.exportKey()
        result = {}
        result["public_pem"] = public_pem
        result["private_pem"] = private_pem
        return result

    # 加密
    def encryption(self, target, public_pem):
        rsakey = RSA.importKey(public_pem)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(target))
        return cipher_text
    # 解密
    def decryption(self, cryptedMessage, privateKey):

        rsakey = RSA.importKey(privateKey)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(cryptedMessage), self.random_generator)
        # print text
        return text

    def random_string(self,length):
        # seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(length):
          sa.append(random.choice(seed))
        salt = ''.join(sa)
        # print salt
        return salt
        #运行结果：l7VSbNEG
        #第二种方法
        # salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        # print salt

    def rsa_long_encrypt(self, public_pem, msg):

        msg = msg.encode('utf-8')
        length = len(msg)
        default_length = 117
        #公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(public_pem))
        #长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        #需要分段
        offset = 0
        res = []
        print("length" + str(length))
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset+default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)
        return base64.b64encode(byte_data)

    def rsa_long_decrypt(self, private_pem, msg):

        msg = base64.b64decode(msg)
        length = len(msg)
        default_length = 128
        #私钥解密
        priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(private_pem))
        #长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(msg, b'xyz'))
        #需要分段
        offset = 0
        res = []

        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(msg[offset:offset+default_length], b'xyz'))
            else:
                res.append(priobj.decrypt(msg[offset:], b'xyz'))
            offset += default_length
        return b''.join(res)