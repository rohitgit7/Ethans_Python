#Python internally does not support method overloading
#There are other ways to achieve it

class overloading():
	def __init__(self, var1, var2):
		self.var1 = var1
		self.var2 = var2
		print "Value of var1(%d) and var2(%d)" %(var1, var2)

	def __str__(self):
		return "Returning a string"

	def __len__(self):
		return 5

	def __add__(self, var):
		return self.var1 + self.var2 + var


obj = overloading(5, 4)
print obj			#calls str method
print len(obj)		#calls __len__() method __len__()
print obj + 1		#Operator overloading call __add__() method