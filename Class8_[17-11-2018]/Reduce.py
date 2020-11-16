#Reduce function reduce continually applies the function func() to the sequence seq

import functools

print functools.reduce(lambda x,y:x+y, [23,54,67,78])
lt1 = range(10)
print functools.reduce(lambda x,y:x+y, lt1)