from timeit import timeit


def time_cal1():
    x1 = (i for i in range(5000))
    print(type(x1), lists(x1)[:5])

def time_cal2():
    x2 = [i for i in range(5000)]
    print(type(x2), x2[:5])

t1 = timeit('time_cal1()','from __main__ import time_cal1', number=10)

t2 = timeit('time_cal2()','from __main__ import time_cal2', number=10)

print(t2-t1)
