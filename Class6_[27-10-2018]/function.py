def hello():
	print "Hello, i m in a function/def"
	print range(1,11)

hello()

def say_hello(name,age,city="Ahmednagar"): #passing an argument
	print "Hello %s age %d city %s" %(name,age,city)

say_hello("Rohit",29)
say_hello("Rohit",29,"Pune") #optional argument should be at last
say_hello(age=29,name="Rohit") #if argument name is specified then there no need to follow sequence

def squares(num):
	return num*num

print squares(2)
print "squares of 3 is %d" %squares(3)

#args
def func1(*num):
	print type(num)
	print len(num)
	print num[2]
	print num

func1(4,5,6,7,8)

#kargs or keyword args
def func2(**num):
	print type(num)
	print len(num)
	print num
	print num['a'] #it will throw an error if it does not find the key 'a'
	print num.get('a') #'a' is a key. If it does not find the key in arguments passed, it will simply ignore without throwing an error

func2(a=3)
