# 高阶函数
# 绝对值
print(abs(-10))

# 函数赋值
f = abs
x = f(-99)
print("x =", x)


# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(a, y, f):
    return f(a) + f(y)


print("sum = ", add(-88, -18, f))


# map 使用
def f(m):
    return m * m


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(" 列表对应的平方1 =", list(r))
print(" 列表对应的平方2 =", r)

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

print("列表转string ", list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce
def add(x, y):
    return x + y
print("sum =", reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y

print("sum001 =",reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print("sum003 =", reduce(fn, map(char2num, '1379')))

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print("sum 004 =", str2int("1868"))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# filter
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#1、获取奇数
def is_odd(n):
    return n % 2 == 1
print("奇数 =", list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()

print("非空 =", filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


print("排序结果为 =", sorted([36, 5, -12, 9, -21]))