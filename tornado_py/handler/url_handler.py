# -*- coding: UTF-8 -*

from tornado_py.handler.login_handler import LoginHandle
from tornado_py.handler.qrcode_handler import QRCodeHandle
from tornado_py.handler.goods_handler import GoodsHandle
from tornado_py.handler.payment_handler import PaymentHandle
from tornado_py.handler.verify_pw_handler import VerifyPassWordHandle


def GetUrlHandle():

    result = []

    result.append((r"/app/login", LoginHandle))
    result.append((r"/app/qr_code", QRCodeHandle))
    result.append((r"/app/goods_info", GoodsHandle))
    result.append((r"/app/payment", PaymentHandle))
    result.append((r"/app/verify_pw", VerifyPassWordHandle))

    return result