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
