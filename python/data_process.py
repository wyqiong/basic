#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# 变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
def enroll(name, gender, age=6, city='Beijing'):
        pass
enroll('Adam', 'M', city='Tianjin')

# 把函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
# *号，把list或tuple的元素变成可变参数传进去
calc(*nums)

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 24, **extra)

def main():
    print(r'\\\t\\')
    # dict 特点：比list速度快，占用内存大
    # 选择不可变对象作为key
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    d.get('Thomas', -1)
    d.pop('Bob')
    print (d)

    # 在set中，没有重复的key, 可用于 list 去重
    s = set([1, 1, 2, 2, 3, 3])
    s.add(4)
    s.remove(4)
    s2 = set([2, 3, 4])
    s & s2
    s | s2

    # for
    for i in list(range(5)):
        pass
    for idx, value in enumerate(['A', 'B', 'C']):
        pass
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        pass
    [m + n for m in 'ABC' for n in 'XYZ']

    d = {'x': 'A', 'y': 'B', 'z': 'C' }
    for k, v in d.items():
        pass
    [k + '=' + v for k, v in d.items()]

    # 生成器
    g = (x * x for x in range(10))
    next(g)


    # list
    classmates = ['Michael', 'Bob', 'Tracy']
    print (classmates[-1])
    classmates.insert(1, 'Jack')
    # 删除末尾
    classmates.pop()
    # 删除下标1的
    classmates.pop(1)

    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    L[0:3]
    L[-2:]
    # every 2
    L[:10:2]
    # duplicate
    L[:]

    # tuple，与list类似，但不可修改
    classmates = ('Michael', 'Bob', 'Tracy')
    t = (1,)
    # ['A', 'B']可以变
    t = ('a', 'b', ['A', 'B'])

    # encode and decode
    'ABC'.encode('ascii')
    # b'ABC'
    # 中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围
    # ???'中文'.encode('utf-8')
    # b'\xe4\xb8\xad\xe6\x96\x87'
    b'ABC'.decode('ascii')
    # b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
    # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
    len('ABC')==3
    len('中文')==2
    len(b'ABC')==3
    #???len('中文'.encode('utf-8'))==6

    print('''line1
     line2
     line3''')

    # map
    list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    from functools import reduce
    # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    def fn(x, y):
        return x * 10 + y
    reduce(fn, [1, 3, 5, 7, 9])
    # 13579
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def str2int(s):
        def fn(x, y):
            return x * 10 + y
        def char2num(s):
            return DIGITS[s]
        return reduce(fn, map(char2num, s))

    # or
    def char2num(s):
        return DIGITS[s]

    def str2int_lambda(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    # filter
    def not_empty(s):
        return s and s.strip()
    list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

    # sorted
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True)
    # ['about', 'bob', 'Credit', 'Zoo']
    # ['Zoo', 'Credit', 'bob', 'about']
if __name__ == '__main__':
    sys.exit(main())
