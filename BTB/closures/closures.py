# nested functions
def sort_by_last_letter(strings):
    def last_letter(s): # last letter is redefined everytime sort by last letter is called
        return s[-1]
    return sorted(strings, key = last_letter)

# scopes
g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l)
    inner()
#closure

def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func


ls = enclosing()
ls()
ls.__closure__


# function factory takes some params, creates a local function, returns new specialized functions
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp) # creates a closure
    return raise_to_exp

square = raise_to(2)
square(5)

# global and nonlocal

import time
def make_timer():
    last_called= None
    def elapsed():
        nonlocal last_called # creates a persisten storage
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return  elapsed



