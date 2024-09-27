def func1():
  print("func1")


def func2():
  print("func2")
  func1()


func2()

def r_func(n):
  print("number " + str(n))
  if n > 0:
    r_func(n-1)

r_func(994)

for i in range(10000000):
  print(i)