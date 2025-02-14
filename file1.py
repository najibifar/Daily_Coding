f = open("demofile.txt", "r")
print(f.read(5))
print(f.readline())
print(f.readline())
for x in f:
    print(x)

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("I:\welcome.txt", "r")
print(f.read())
print(f.read(20))
print(f.readline())