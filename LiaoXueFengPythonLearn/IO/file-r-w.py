#!/usr/bin/env python
# encoding: utf-8

######　１.读文件
>>> f = open('F:/test.txt', 'r')　# r:读取UTF-8编码的文本文件
>>> f = open(r'f:\test.txt','r')
>>> f.read() #文件打开成功后，就可以调用read()方法，一次读取文件的全部内容
'hello world'  #Python把内容读到内存，用一个str对象表示
>>> f.close()  #最后一步调用close()将文件关闭
>>>
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 为保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
try:
    f = open('F:/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 为简化书写，引进with
with open('F:/test.txt', 'r') as f:  #和前面的try...finally一致
    print(f.read())
# read()  一次读取全部内容
#read(size) 每次最多读取size字节的内容
# readline()  每次读取一行
# readlines()  一次读取所有内容并按行返回lisi
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉