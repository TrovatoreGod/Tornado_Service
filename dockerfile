#基础镜像
FROM python:2.7

#作者信息
MAINTAINER wzl

#复制当前目录全部文件到工作目录
#COPY ./ /MyTest

#工作目录
WORKDIR /MyTest

RUN python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install tornado -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install python-memcached -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install pycrypto -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install python-dateutil -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install Flask-SQLAlchemy -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install enum34 -i https://pypi.tuna.tsinghua.edu.cn/simple

#指定端口（不建议使用）
#EXPOSE 8899

# 变参
CMD ["python","tornado_py/website_service.py"]

