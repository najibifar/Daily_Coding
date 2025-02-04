thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)