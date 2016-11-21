d = {'banana': 3, 'apple':4,'pear': 1, 'orange': 2}
a = sorted(d.items(), key=lambda t: t[0])
print a
b = sorted(d.items(), key=lambda t: t[1])
print b
