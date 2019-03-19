# modify or enhance functions without changing their definition
# improve maintaibabilty, readbility, scalability of deisngs


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs) # use *args and **kwargs to take any number of arguments
        return ascii(x)
    return wrap


def _bin(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs) # use *args and **kwargs to take any number of arguments
        return x.upper()
    return wrap


@escape_unicode
@_bin
def vegetable():
    return 'blomkå∂∆©ƒ®©l'




