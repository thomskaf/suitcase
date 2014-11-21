"""
    faster.py
    ~~~~~~~~~

    :licence: none, Public Domain.
"""
from timeit import timeit


# Calling out to methods written in C is usually quicker than running
# interpreted code.
i = timeit(stmt='while i < 10 ** 8: i += 1', setup='i = 0', number=1)
c = timeit(stmt='for i in range(0, 10 ** 8): i += 1', setup='i = 0', number=1)

# Joining rather than concatenate.
setup = """
def concat_str(limit):
    resp = ''
    for num in range(limit):
        resp += 'num'
    return resp
"""
concatenate = timeit(stmt='concat_str(2 ** 20)',
                     setup=setup,
                     number=10)

setup = """
def join_list(limit):
    return ''.join(['num' for num in range(limit)])
"""
join = timeit(stmt='join_list(2 ** 20)',
              setup=setup,
              number=10)


# List comprehensions over loops.
setup = """
def join_list(limit):
    resp = []
    for num in range(limit):
        resp.append('num')
    return ''.join(resp)
"""
list_loop = timeit(stmt='join_list(2 ** 20)',
                   setup=setup,
                   number=10)
setup = """
def join_list(limit):
    return ''.join(['num' for num in range(limit)])
"""
list_comp = timeit(stmt='join_list(2 ** 20)',
                   setup=setup,
                   number=10)


# List is slower than set.
a_list = timeit(stmt='"9" in string',
                setup='string = list("abcefg0123456789")',
                number=10 ** 8)

a_set = timeit(stmt='"9" in string',
               setup='string = set("abcefg0123456789")',
               number=10 ** 8)

if __name__ == "__main__":
    print("""C code usually outruns interpreted code:
I: %f
C: %f

Joining rather than concatenate:
join  : %f
concat: %f

List comprehensions over loops:
comp: %f
loop: %f

List is slower than set:
list: %f
set : %f""" % (i, c, join, concatenate, list_comp, list_loop, a_list, a_set))
