s = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"

l = []
m = []
o = []
e = []

for i in s:
    if i >= 'a' and i <= 'z':
        l.append(i)

for j in s:
    if j >= 'A' and j <= 'Z':
        m.append(j)

for k in s:
    if k.isdigit():
        if int(k)%2 == 1:
            o.append(k)
        if int(k)%2 == 0:
            e.append(k)





m.sort()
l.sort()
o.sort()
e.sort()


c = ''.join(l)
d = ''.join(m)
f = ''.join(o)
g = ''.join(e)

print (c + d + f + g)




