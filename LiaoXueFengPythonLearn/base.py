#!/usr/bin/env python
# encoding: utf-8

######  1、list/tuple
### 1.1 list列表
classmates=['Bob','Michael','Amy'] #Python内置的一种数据类型是列表，可插入、删除
classmates.append('Adam') # 在末尾扩展元素Adam
classmates.insert(1,'Jack') #在指定索引位置插入元素
classmates.pop() #删除末尾的元素
classmates.pop(i)#删除指定索引位置的元素
classmates[1]='Sarah'#赋值
### 1.2 tuple元组
classmates=('Bob','Michael','Amy')#tuple和list非常类似，但是tuple一旦初始化就不能修改

###### 2、dict/set
### 2.1 dict 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}#键值对 key_value
d.get('Bob')#获取值
d.pop('Bob')#删除
### 2.2 set
s=set([1,2,3])#key的集合，不存储value，且key不能重复。创建set，以list作为输入集合。无序
s.add(key)#添加元素
s.remove(key)#删除元素
s1&s2 #无序和无重复元素的集合，可做交集、并集操作

###### 3、逻辑
### 3.1 条件判断
if age >= 18:
    print('adult')
### 3.2 for循环
sum = 0
for x in range(101):  #range(101)生成0-100的整数序列
    sum = sum + x
print(sum)

### 3.3 while 循环
 sum=0
 n=99
 while n>0:
    sum=sum+n
    n=n-2
print (sum)


