def it_is_true(anything):
    if anything:
        print('yes it\'s true')
    else:
        print("no it\'s false")


a_list = ['a', 'b', 12312]
print(a_list[2])
print(a_list[1:3:2])


b_list = a_list[:]
a_list[0] = 'hello'
print(a_list, b_list)


# insert to the beginning of a list
a_list.insert(0, 'œ')
print(a_list, b_list)


# extend will add each individual item to the list
a_list.extend(['hello', 456])
print(a_list)

a_list.append(['hello', 456])
print(a_list)
print(type(a_list[-1]))
print(a_list[0:len(a_list):2])


# searching for values
print(a_list.count('hello'))


# removing values
a_list.remove('hello')
print(a_list)

# Tuples
# faster than lists, write protected
a_tuple = ("a", "b", "hspivey")

# assign multiple values at once
v = ('a', 2, True)
(x, y, z) = v
print(x, y, z)

# sets
a_set = {1}
a_set.add(42)
a_set.update({1, 42, 3, 5, 6, 7, 8})
a_set.update([6, 7, 8, 9])
print(a_set)

a_set.discard(43)
# a_set.remove(43) -> keyError

# completely arbitrary
a_set.pop()
a_set.pop()
a_set.pop()

a_set.clear()  # -> removes all values from a set
