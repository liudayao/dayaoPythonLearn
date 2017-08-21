#!/usr/bin/env python
# encoding: utf-8


###### 1、切片
L=[0,1,2,3,4,5,6,7,8,9,10]
L[:10:2]#[0,2,4,6,8] 从第0到10位
L[::2]#[0,2,4,6,8,10] 所有的数，每隔2个取1个
L[0:3]#[1,2,3]

###### 2、迭代
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
 #迭代value，用for value in d.values()。同时迭代key和value，用for k, v in d.items()

###### 3、列表生成式
[x * x for x in range(1, 11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 [x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]
 [m + n for m in 'ABC' for n in 'XYZ']#使用两层循环，生成全排列；['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

###### 4、生成器 generator
 g = (x * x for x in range(10))
 for n in g:                   #一边循环一边计算
	print(n)

###### 5、迭代器
from collections import Iterable
  #可以直接作用于for循环的对象统称为可迭代对象：Iterable
isinstance('abc', Iterable)#True,使用isinstance()判断一个对象是否是Iterable对象
  #可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
isinstance('abc', Iterator)#False,使用isinstance()判断一个对象是否是Iterator对象
  #凡是可作用于for循环的对象都是Iterable类型；
  #凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
  #集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
  #Python的for循环本质上就是通过不断调用next()函数实现的
