# -*- coding: UTF-8 -*-

import os
import sys

#this_folder = os.path.dirname(os.path.abspath(__file__))
#os.chdir(this_folder)
#sys.path.append(os.path.join("E:/PythonFile/tornado_service", ".."))
import tornado.web
import tornado.ioloop
import tornado.options  # 让模块有自定义选项
import tornado.httpserver  # 启动一个单线程的http服务器
from tornado.options import define, options
from handler.url_handler import GetUrlHandle

# 定义端口号
# help:帮助提示
define("port", default=8088, help="given your port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handle = GetUrlHandle()
        # 配置
        settings = dict(
            debug=True,
            private_key="-----BEGIN RSA PRIVATE KEY-----"
                        "\nMIICXAIBAAKBgQCh8A4vxJSHLQlSMYHEDCay/nlpTAvB/I2pLkcLkMT3PaSMhmaN"
                        "\nfldugT65NR/UPtrY+hG3WzJ9LlfEJEc4rQ7W5l2VKKZW2VCtOf9EEt4g1orcRWoa"
                        "\nnfhz6EfuQ3HZMc9Z9xi3BHGZAlEq5L0fksnD/8ZTW268DH0cPK4cL+5pHwIDAQAB"
                        "\nAoGAETjwqU/k5AN8LEurm2gXbY3256X40ibEAiwzzh0VdZ4OtAtPONko/02rmBL4"
                        "\nUaBlshHWdIO0eO/G0ctx76soGrOLPbbw6fDYmgGSEkI7LiPUHLbV4kkwdp/uQDQQ"
                        "\nknZPIUYAtNOMbmdz2GqB2FnoaR0fXyQLRAeKnPWMwbQxEEECQQDEeaENdZ4Bg9m5"
                        "\nrm7wEy1smobJS4/9AHKWXbHG+s3kHxnb6Ss717mqRRMNCKLDmsH68EMaxBxfeHSO"
                        "\neFNbtZJPAkEA0v+/biymRFnCmYJGne2uxG3tNq4JYJeisShNlxoHArQDGD+Hg4Ex"
                        "\nQOYezuFpf792LDERYD0Frc14S1i0TKoYMQJANFNoTxtZ/3FMFSWdqhaRbHEjII0d"
                        "\nRfZOjjlZ1XKKTwzxaB4LQ57Kdcx7rGb2Yj3fF6PRW1mLbOm5sQ/es3gCBQJAOS3V"
                        "\nUqYG6L7qXW9Qc7vVgKXJgufm4qY1EI07eZc0Dyd5LzkIIDsCffPepXGwhU39WDxz"
                        "\n2QCwaUklMEX5lk0CAQJBAJtzFgzp1al6vuqwpIoKFNHRxkxNzwVj7VxWAcps8ePK"
                        "\n4YDHHzhQq2Pi8DB1aNBWwyxtG7kijQ1gEnU/EKM7ukg="
                        "\n-----END RSA PRIVATE KEY-----",
        )

        tornado.web.Application.__init__(self, handle, **settings)


def main():
    if os.name == "nt":
        tornado.options.parse_command_line()  # 可以通过命令行交互 python xxx.py --port=8888
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(options.port)  # 调用自定义端口
        instance = tornado.ioloop.IOLoop.instance()
        # autoreload的实现原理是将各个文件的路径和文件的修改时间缓存起来；然后利用ioloop.py，
        # 定时得去check各个文件目前的修改时间和缓存中的时间是否一致，如果不一致，则加载
        tornado.autoreload.start(instance)
        instance.start()
    else:
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.bind(options.port)
        http_server.start(0)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
