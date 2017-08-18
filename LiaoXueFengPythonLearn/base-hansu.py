#!/usr/bin/env python
# encoding: utf-8

###### 1、函数
### 1.1 函数的参数
# 1.1.1 默认参数
def power(x,n=2);#定义函数时，把参数n默认设置成2。默认参数必须指向不变对象
power(5);#等于power(5,2)
power(5,3);#当n不等于2时，就需要传入n
# 1.1.2 可变参数
def calc(*numbers):#在参数前面加了一个*号，参数numbers接收到的后自动形成一个turple
calc(1,2,3)#调用函数时，可传入任意个参数
L=[1,2,3,4]
calc(*L)#将列表L的所有元素作为可变参数
# 1.1.3 关键字参数
def person(name, age, **kw):#关键字参数允许传入任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
person('Michael', 30)
person('Bob', 35, city='Beijing')#可只传必选参数，也可再传任意个关键字参数
person('Adam', 45, gender='M', job='Engineer')
person(name, age, **)d#将dict-d中的所有元素作为关键字参数传入
# 1.1.4 命名关键字参数
def person(name, age, *, city, job):#限制关键字参数的名字，*后面的参数被视为命名关键字参数
person('Jack', 24, city='Beijing', job='Engineer')#命名关键字参数必须传入参数名
# 1.1.5 参数组合
     #定义参数顺序必须为：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
### 1.2 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

###### 2、函数式编程
### 2.1 高阶函数          函数的参数也是个函数
# 2.1.1 map/reduce
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])#将函数f依次作用予序列的每个元素上，并把结果作为一个新的list返回；
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)#把函数f作用在序列元素上，f必须接受2个参数，reduce把结果继续和序列的下一个元素做累积计算
# 2.1.2 filter()               用于过滤函数
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))#接收一个函数和序列，将传入的函数依次作用于每个元素，然后根据返回值True/False决定保留还是丢弃该元素。
# 2.1.3 sorted()               对list进行排序
sorted([36, 5, -12, 9, -21])
sorted([36, 5, -12, 9, -21], key=abs) #可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序











