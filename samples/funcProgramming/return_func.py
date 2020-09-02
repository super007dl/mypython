
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print("sum 返回的是对象=", f)
print("f() =", f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 5):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 , f4 = count()

print("f1() =", f1())
print("f2() =", f2())
print("f3() =", f3())


# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print("new f1() =", f1())
print("new f2() =", f2())
print("new f3() =", f3())


# 匿名函数
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print("L =", L)

# decorator

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print("now() =", now())



def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

print(now())

#########################################################
####################partial############################
#########################################################

import functools
int2 = functools.partial(int, base=2)
print("int2('1000000') =", int2('1000000'))



