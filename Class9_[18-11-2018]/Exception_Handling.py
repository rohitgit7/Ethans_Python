#try:
#except:
#else: will execute only if there is no exception is thrown
#finally: Always runs this code. If there is 'return' in try block then finally block will get executed before return statement

dict1 = {1:'one',2:'two'}
print "dict1[2]",dict1[2]
'''
try:
	print "Lets check keys..."
	print dict1[3]
	print "looks good"
except:
	print "Does not have this key"
'''
def test():
	try:
		#import xyz
		print "import xyz completed"
		return "try"	#finally block will get executed before this return
	except KeyError:
		print "Got key error"
	except ImportError as error:	#error contains the error message thrown by ImportError
		print "Got import error"
		print error
	else:
		print "Yayy! No errors"
	finally:
		print "This is a finally block"
		return "finally"

#test()
print test()
