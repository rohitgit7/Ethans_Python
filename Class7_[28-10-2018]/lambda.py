#lambda functions
x = lambda a : a*a
print x(2)

fun = lambda a,b : a*b #fun is reference to lambda function
print fun(3,4)

def test(n):
	return lambda a : a+n #returns lambda function lambda a : a+n
print test(3) #lambda a : a+3 will return reference

lam = test(10) #lambda a : a+10
print lam(6) #lambda 6 : 6+10 will return 16
