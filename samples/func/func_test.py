
# 函数的调用
a = abs(-100)
print("a =", a)

ab = abs
print(ab(-999))


# 自定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-888))

# print(my_abs("sdaga"))

print(my_abs(-888999))

# 函数参数
def fact(n):
    if n==1:
        return n
    return n * fact(n-1)

print(fact(1))
print(fact(5))