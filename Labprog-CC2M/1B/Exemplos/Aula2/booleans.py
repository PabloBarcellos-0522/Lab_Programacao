print(10 > 5)
print(10 == 5)

print(bool("a"))
print(bool(""))
print(bool(0))

class myClass:
  def __len__(self):
      return 0


myobj = myClass()
print(bool(myobj))
