# -*- coding: UTF-8 -*-

import tornado.web
import json
import traceback
from tornado_py.util.cryptorsa import rsacrypt


class PaymentHandle(tornado.web.RequestHandler):

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
                order_num = request_json["order_num"]
                goods_info = {"order_num": order_num, "order_status": True}
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

            print "payment---" + request_data
