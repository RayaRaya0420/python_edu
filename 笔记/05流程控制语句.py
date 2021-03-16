# if：关键字
# 官方推荐：缩进为四个空格

# 单if
# if 条件 冒号
# 缩进 结果
if 3>2:
    print(1)

# if else 二选一
# if 条件 冒号
# 缩进 结果
# else 冒号
# 缩进 结果
if 3>2:
    print(1)
else:
    print(2)

# if elif elif 多选一或零
a = int(input("please enter"))
if a == 0:
    print('equal')
elif a < 0:
    print('less than')
elif a > 0:
    print('great than')