s = "Enter a alphanumeric string" input() 

l = [] 
u = []
o = []
e = []

for i in s:
    if i >= 'a' and i <= 'z':
        l.append(i)

for j in s:
    if j >= 'A' and j <= 'Z':
        u.append(j)

for k in s:
    if k.isdigit():
        if int(k)%2 == 1:
            o.append(k)
        if int(k)%2 == 0:
            e.append(k)

l.sort()
u.sort()
o.sort()
e.sort()

c = ''.join(l)
d = ''.join(u)
f = ''.join(o)
g = ''.join(e)

print (c + d + f + g)
