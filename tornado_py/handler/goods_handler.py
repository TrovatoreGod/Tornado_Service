# -*- coding: UTF-8 -*-

import tornado.web
import json
import traceback
from tornado_py.util.cryptorsa import rsacrypt
import MySQLdb


class GoodsHandle(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write("Not support get requests")

    def post(self, *args, **kwargs):
        self.get_data()

    def get_data(self):
        result = {"status": False, "data": ""}
        request_argument = self.get_argument("data", "")
        # parameters is null
        if request_argument == "":
            self.write("request data is null")
        else:
            # get private_key from application.settings
            private_key = self.application.settings.get("private_key")
            rsa1 = rsacrypt()
            data = rsa1.rsa_long_decrypt(private_key, request_argument)
            try:
                tuple_request = (True, json.loads(data))
                # return tuple_request
            except Exception as e:
                traceback.print_exc()
                print("REQUEST_JSON" + e.message)
                self.write(e.message + "")

            if tuple_request[0]:
                request_json = tuple_request[1]
                goods_id = request_json["goods_id"]
                goods_info = self.query_goods_data(goods_id)
                goods_info["order_num"] = 123456789
                try:
                    result["data"] = goods_info
                    result["status"] = True
                except Exception as e:
                    print("REQUEST_JSON" + e.message)
                    result["data"] = {}
                    result["status"] = False
                finally:
                    pass
                request_data = json.dumps(result)
                self.write(request_data)
            else:
                request_data = json.dumps(result)
                self.write(request_data)
            print "goods_info---" + request_data

    def query_goods_data(self, goods_id):
        # 建立和数据库的连接
        try:
            db = MySQLdb.connect(host="192.168.1.100", user="root", passwd="root123", db="vending_machine",
                                 charset='utf8')
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("MySQLdb" + e.message)
            self.write(e.message + "")
        # 获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM VM_GOODS_INFO WHERE goods_id = " + goods_id
        user_data = {}
        # 执行sql
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for text in results:
                user_data["goods_id"] = text[0]
                user_data["goods_name"] = text[1]
                user_data["price_unit"] = text[2]
                user_data["goods_price"] = text[3]
                user_data["payment_way"] = text[4]
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("MySQLdb" + e.message)
            self.write(e.message + "")
        # 关闭连接，释放资源
        db.close()

        return user_data
