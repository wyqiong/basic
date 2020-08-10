import sys
import functools


class Student(object):
    # 类属性
    name = 'Student'

    def __init__(self, name, score):
        # 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        # 以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        # 实例属性
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

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