#基础镜像
FROM python:2.7

#作者信息
MAINTAINER wzl

#工作目录
WORKDIR /MyTest

#复制当前目录全部文件到工作目录
#OPY ./ ./MyTest

RUN python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple&&pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

#指定端口（不建议使用）
#EXPOSE 8899

# 变参
CMD ["python","./tornado_py/website_service.py"]

