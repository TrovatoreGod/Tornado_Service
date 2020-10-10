# -*- coding: UTF-8 -*-

import tornado.web
import json
import traceback
from tornado_py.util.cryptorsa import rsacrypt
import MySQLdb


class LoginHandle(tornado.web.RequestHandler):

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
                user_account = request_json["user_account"]
                user_data = self.query_user_data(user_account)
                if user_data == {}:
                    result["data"] = {}
                    result["status"] = False
                    request_data = json.dumps(result)
                    self.write(request_data)
                else:
                    try:
                        result["data"] = user_data
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
            print "login---" + request_data

    def query_user_data(self, account):
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
        sql = "SELECT * FROM VM_USER WHERE user_account = '" + account + "'"
        user_data = {}
        # 执行sql
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for text in results:
                user_data["user_id"] = text[0]
                user_data["user_account"] = text[1]
                user_data["user_type"] = text[2]
                user_data["user_status"] = text[3]
                create_date = text[4]
                user_data["create_date"] = create_date.strftime("%Y-%m-%d")  # "%Y-%m-%d %H:%M:%S"
                user_data["pass_word"] = text[5]
                user_data["user_name"] = text[6]
                user_data["user_tel"] = text[7]
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("MySQLdb" + e.message)
        # 关闭连接，释放资源
        db.close()

        return user_data
