x = ("aaa", "bbb", "ccc", "ddd")
y = list(x)
y[1] = "eee"
x = tuple(y)
print(x)