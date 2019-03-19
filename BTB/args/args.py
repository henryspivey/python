# using *args
def hypervolume(length, *lengths):
    # *lengths will be passed as a tuple
    v = length # required parameter
    for item in lengths:
        v *= item
    return v

print(hypervolume(3,5,6,9))
print(hypervolume(3,5,9))
print(hypervolume(3,5))
print(hypervolume(3))
#print(hypervolume())

#using **kwargs

def tag(name, **attributes):
    result = '<'+name
    for key,value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v= str(value))
    result += '>'
    return result

print(tag('img', src="monet.jpg", alt="Sunrise", border=1))


def color(r, g, b, **kwargs):
    print("r = ", r)
    print("g = ", g)
    print("b = ", b)
    print(kwargs)

k = {'r': 21, 'g':68, 'b': 120, 'alpha':52}
color(**k)

def trace(f, *args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result = ", result)
    return result

trace(int, "ff", base=16)


# zip function
"""
takes 2 iterable series and returns a pair of elements of both series together in a tuple
"""

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20]
monday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20]
for item in zip(sunday, monday):
    print(item)

daily = [sunday, monday]
# could do it with
for item in zip(daily[0], daily[1]):
    print(item)

# better with
for item in zip(*daily):
    print(item)

