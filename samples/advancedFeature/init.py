L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)



# 2. 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n +1
    return "done"

