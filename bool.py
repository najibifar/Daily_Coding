class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


print(bool("abc"))

print(bool(0))
print(bool(1))

fruits = ["apple", "banana"]
if "apple" in fruits:
