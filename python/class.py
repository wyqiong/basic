import sys
import functools


class Student(object):
    # 类属性
    name = 'Student'
    # 用tuple定义允许绑定的属性名称
    # 仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('me', 'age') 
    def __init__(self, name, score):na
        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        # 以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        # 实例属性
        self.__name = name
        self.__score = score

    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    # 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def score(self):
        return self._score
    # 检查参数
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    '''
    >>> for n in Fib():
    ...     print(n)
    ...
    1
    1
    2
    '''
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    '''
    >>> f = Fib()
    >>> f[0]
    1
    >>> f[1]
    1
    '''
    def __getattr__(self, attr):
        if attr=='score':
            return 99

# restful api
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    '''
    >>> Chain().status.user.timeline.list
    '/status/user/timeline/list'
    '''

#
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
# mixin
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

# 获取对象信息
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj, 'x'）
obj.x
setattr(obj, 'y', 19)
getattr(obj, 'z', 404)


def log(func):
    # 把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def main():
    print('2015-3-25')

    # 偏函数
    int2 = functools.partial(int, base=2)
    int2('1000000')
    # 64

if  __name__ == '__main__':
    sys.exit(main())