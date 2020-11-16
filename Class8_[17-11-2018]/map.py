#Map function maps all items in list as input items to the called function

#SYNTAX: map(function_to_apply, list_of_inputs)

def square(x):
	return x*x

list1 = [1,2,3,4]
print map(square,list1)

str = ['1','2','3']
print map(int,str) #converts string to integer

sq = map(lambda x:x**2,list1)
print sq

def add(x):
	return x+x

def multi(x):
	return x*x

funcs = [add,multi]
print "Type of funcs[0]",type(funcs[0])

for i in range(5):
	value = list(map(lambda x:x(i),funcs))
	print value



