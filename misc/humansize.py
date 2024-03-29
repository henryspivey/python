SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator


@rename('testing')
def approximate_size(size=0, a_kilo_byte_is_1024_bytes=True):
    '''Convert a file size to human readable form

    Keyword Arguments:
    size -- file size in bytes
    a_kilo_byte_is_1024_bytes -- if True (default), use multiples of 1024

    if False, use multiples of 1000

    returns string 
    '''

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilo_byte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(10**24, False))
    print(approximate_size(1000000000000))
    print(approximate_size.__name__)
