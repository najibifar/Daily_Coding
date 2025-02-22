d = {}
for a in range(2):
 for b in range(5):
    d[a] = b
print(d)


s = 'robot'
a, b, c, d, e = s
b = d = '*'
s = (a, b, c, d, e)
print(s)

x = "Python" 
print(x[2:5])


set1 = {10, 20, 30} 
set2 = set1.remove(20) 
print(set2)

def extend_list(lst): 
    lst.extend([10]) 
    b = [5, 10, 15, 20] 
    extend_list(b)
print(len(b))

queue = {'name', 'age', 'DOB'} 
print(queue) 