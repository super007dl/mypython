# 注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# -*- coding: utf-8 -*-


# 转义字符串 [I'm "OK"!]
print('I\'m \"OK\"!')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print("n = ", n)
print("f = ", f)
print("s1 = ", s1)
print("s2 = ", s2)
print("s3 = ", s3)
print("s4 = ", s4)


# 赋值问题
a = "abd"
b = a
a = "xyz"
print("a=", a, "b=", b)

# 数据
print("9/3 =", 9/3)
print("10/3 =", 10/3)
print("10//3 =", 10//3)
print("10%3 =", 10 % 3)

print("我爱你中国")


# 占位符
print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

name = 'ricky'
print(f'hello {name}!')

# list
classMates = ["ricky", "tarai", "lily"]
print("classMates = ", classMates)
print("classMates.length = ", len(classMates))
print(classMates[0])
print(classMates[-1])
print(classMates[-2])

classMates.append("adm")
classMates.insert(1, "cheche")

print(classMates)


classMates.pop()
classMates.pop(1)
print(classMates)


classMates[1] = "licky"
print(classMates)


L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(L, s, len(L), len(s))

# tuple
t = ["a", "b", ["c", "d"]]
print("t = ", t)
t[2][0] = "X"
t[2][1] = "Y"
print("t1 = ", t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 获取php
print("php =", L[1][3])


# 条件判断
age = 20
if age >= 18:
    print("you age is", age)
    print("adult")
else:
    print("you age is", age)
    print("teenager")


# s = input('birth: ')
# birth = int(s)
# if birth >= 2000:
#     print("00后")
# else:
#     print("00前")


# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sumNum = 0
for x in [1, 2, 3, 4, 5, 6]:
    sumNum = sumNum + x
print("sumNum = ", sumNum)

num = list(range(5))
print("list =", num)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 4
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("end")

n = 1
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print("n =", n)


# 字典 dict
d = {"ricky": 15, "tarai": 22}
print(d["tarai"])

d["tarai"] = 55
print(d["tarai"])

d["ricky1"] = 33
print("d[ricky1] =", d["ricky1"])
# print("d[ricky2] =", d["ricky2"])

d.pop('ricky1')
# print("d[ricky1] =", d["ricky1"])


# set
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 5}
print(set1 & set2)
print(set1 | set2)

a = ['c', 'b', 'a']
a.sort()
print("a =", a)


str1 = 'abc'
str2 = str1.replace("a", "A")
print("str1 =", str1, str2)