from re import X


def myfunc():
   global x
   x = "fantastic"

myfunc()

print("Python is " + x)
