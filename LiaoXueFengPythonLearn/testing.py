#!/usr/bin/env python
# encoding: utf-8

###### 1.错误处理

### 1.1 try...except...finally...
try:                     #当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行；
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:    ## 跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块.
    print('ValueError:', e)
except ZeroDivisionError as e:    ##可以有多个except来捕获不同类型的错误
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

### 1.2.调用堆栈     #如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
# err.py:
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    bar('0')
main()
#执行结果
''' $ python3 err.py
Traceback (most recent call last):  #错误的跟踪信息。
  File "err.py", line 11, in <module>  #调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行
    main()
  File "err.py", line 9, in main  #调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行
    bar('0')
  File "err.py", line 6, in bar #原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看
    return foo(s) * 2
  File "err.py", line 3, in foo #原因是return 10 / int(s)这个语句出错了
    return 10 / int(s)
ZeroDivisionError: division by zero  #错误类型ZeroDivisionError，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头
'''
### 1.3 记录错误
import logging   #Python内置的logging模块可以非常容易地记录错误信息

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
#执行结果
''' ERROR:root:division by zero   #同样是出错，但程序打印完错误信息后会继续执行，并正常退出
Traceback (most recent call last):
  File "err_logging.py", line 13, in main      #通过配置，logging还可以把错误记录到日志文件里
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
'''

### 1.4 抛出错误
class FooError(ValueError): #如果要抛出错误，根据需要，可定义一个错误的class，选择好继承关系后，用raise语句抛出一个错误的实例
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
#执行程序
''' $ python3 err_raise.py
Traceback (most recent call last):
  File "err_throw.py", line 11, in <module>
    foo('0')
  File "err_throw.py", line 8, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
'''


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:   #在bar（）中捕获错误，便于后续追踪。
        print('ValueError!')
        raise #为了程序能继续运行，把错误抛给上一层处理。raise语句如果不带参数，就会把当前错误原样抛出
bar()


###### 2、调试
### 2.1 断言(assert)
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  #如果断言失败，assert语句本身就会抛出AssertionError
    return 10 / n
def main():
    foo('0')
#执行后
'''Traceback (most recent call last):
  ...
AssertionError: n is zero!
'''
#  $ python3 -O err.py  启动Python解释器时可以用-O参数来关闭assert

### 2.2 logging
import logging
logging.basicConfig(level=logging.INFO) #指定记录信息的级别，有debug，info，warning，error等几个级别
s = '0'
n = int(s)
logging.info('n = %d' % n)  #logging.info()就可以输出一段文本
print(10 / n)
#运行后
'''
$ python3 err.py
INFO:root:n = 0
Traceback (most recent call last):
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
'''
