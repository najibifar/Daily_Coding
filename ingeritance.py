class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

def myfunc():
  x = 300
  print(x)

myfunc()


def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


x = 300

def myfunc():
  print(x)

myfunc()

print(x)


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


def myfunc():
  global x
  x = 300

myfunc()

print(x)



x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


x = 300
def myfunc():
  x = 200
myfunc()
print(x)


x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)


x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)