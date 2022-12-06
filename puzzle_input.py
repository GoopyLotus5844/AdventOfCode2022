import re

def read(file, commands, section = 0):
    data = open(file, "r").read().split('<--->\n')[section]
    return multiSplit(data, commands)

def multiSplit(data, c):
    d = data.strip()
    if len(c) == 0:
        return tryConvert(d)
    if type(c[0]) is int or len(re.split(c[0], d)) != 1:
        return [multiSplit(i, c[1:]) for i in (re.split(c[0], d) if (type(c[0]) is str) else [d[:c[0]], d[c[0]:]])]
    return d

def tryConvert(val):
    try: return int(val)
    except ValueError: return val