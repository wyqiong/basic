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

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    # 既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 多态

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