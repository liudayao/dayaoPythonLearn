#!/usr/bin/env python
# encoding: utf-8


###### 1����Ƭ
L=[0,1,2,3,4,5,6,7,8,9,10]
L[:10:2]#[0,2,4,6,8] �ӵ�0��10λ
L[::2]#[0,2,4,6,8,10] ���е�����ÿ��2��ȡ1��
L[0:3]#[1,2,3]

###### 2������
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
 #����value����for value in d.values()��ͬʱ����key��value����for k, v in d.items()

###### 3���б�����ʽ
[x * x for x in range(1, 11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 [x * x for x in range(1, 11) if x % 2 == 0] #[4, 16, 36, 64, 100]
 [m + n for m in 'ABC' for n in 'XYZ']#ʹ������ѭ��������ȫ���У�['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

###### 4�������� generator
 g = (x * x for x in range(10))
 for n in g:                   #һ��ѭ��һ�߼���
	print(n)

###### 5��������
from collections import Iterable
  #����ֱ��������forѭ���Ķ���ͳ��Ϊ�ɵ�������Iterable
isinstance('abc', Iterable)#True,ʹ��isinstance()�ж�һ�������Ƿ���Iterable����
  #���Ա�next()�������ò����Ϸ�����һ��ֵ�Ķ����Ϊ��������Iterator
isinstance('abc', Iterator)#False,ʹ��isinstance()�ж�һ�������Ƿ���Iterator����
  #���ǿ�������forѭ���Ķ�����Iterable���ͣ�
  #���ǿ�������next()�����Ķ�����Iterator���ͣ����Ǳ�ʾһ�����Լ�������У�
  #��������������list��dict��str����Iterable������Iterator����������ͨ��iter()�������һ��Iterator����
  #Python��forѭ�������Ͼ���ͨ�����ϵ���next()����ʵ�ֵ�
