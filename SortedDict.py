def SortedDict(dict, wrap="key"):
    if wrap is "key":
        return sorted(d.items(), key=lambda t: t[0])
    if wrap is "value":
        return sorted(d.items(), key=lambda t: t[1])

d = {'banana': 3, 'apple':4,'pear': 1, 'orange': 2}
print(SortedDict(d))
print(SortedDict(d,"value"))
