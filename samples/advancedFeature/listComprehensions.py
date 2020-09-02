
# 1、要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))

# 2、但如果要生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)


# 2.1
print([x * x for x in range(1, 11)])

# 2.2
print([x * x for x in range(1, 11) if x % 2 == 0])


# 3、使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# 4、转小写
L = ['Hello', 'World', 'IBM', 'Apple']

print( [s.lower() for s in L])

# 5、if else
print([x if x % 2 == 0 else -x for x in range(1, 11)])