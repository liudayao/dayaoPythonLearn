#!/usr/bin/env python
# encoding: utf-8

###### 1.面向对象编程
### 1.1 类和实例
class Student(object): #定义类
    def __init__(self, name, score): #绑定name、score属性
        self.name = name
        self.score = score
    def print_score(self): #在类里面定义方法，数据封装
        print('%s: %s' % (self.name, self.score))   #在类中定义的函第一个参数永远是实例变量self，但调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别
bart = Student('Bart Simpson', 59) #创建实例
bart.name #Bart Simpson
bart.name='Bob'
print_score(bart)#'Bob,59   ,调用类方法


### 1.2 访问限制
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score   #实例的变量名以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
>>> bart = Student('Bart Simpson', 98)
>>> bart.__name #报错

class Student(object):
    ...
    def get_name(self):
        return self.__name  #加上get方法，可通过bart.get_name()获取变量
    def set_score(self, score):
        self.__score = score  #加上set方法，可通过set_name修改变量值


### 1.3 继承和多态
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')#当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类，在代码运行的时候，总是会调用子类的run()。
		                          #这样，我们就获得了继承的另一个好处：多态
#静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了

### 1.4 获取对象信息
# 1.4.1 type()
>>> type(123)  #获取对象的类型
<class 'int'>
>>> type('abc')==type('123')
True

# 1.4.2 isinstance()
>>> isinstance(h, dog)#判断对象是否是dog类
True  #能用type()判断的基本类型也可以用isinstance()判断，但type不能用来判断类
isinstance([1, 2, 3], (list, tuple)) #判断变量是否是某类型中的一种

# 1.4.3 dir()
dir('ABC') #获取一个对象的所有方法和属性
['__add__', '__class__','upper', 'zfill'] 

### 1.5 实例属性和类属性
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student#在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性


###### 2、面向对象高级编程
### 2.1 使用__slots__
def set_age(self, age):
...     self.age = age
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法，给一个实例绑定的方法，对另一个实例是不起作用的
Student.set_score = set_score#为了给所有实例都绑定方法，可以给class绑定方法
							 #通常是在类的定义中绑定方法，动态绑定允许我们在程序运行的过程中动态给class加上功能
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义在运行过程中允许绑定的属性名称，__slots__只对当前类有效，对子类无效。


### 2.2 使用@property
class Student(object):

    @property   #@property装饰器：把一个方法变成属性调用；把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):
        return self._score

    @score.setter  #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()

### 2.3 多重继承
class Dog(Animal, Runnable): #dog同时继承animal和Runnerble的功能，主线是Animal，为了更好的看出继承关系，我们把主线之外的继承加上MixIn。
    pass
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn)#多重继承
    pass

### 2.4 定制类

### 2.5 使用枚举类

### 2.6 使用元类