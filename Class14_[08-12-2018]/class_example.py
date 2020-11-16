class exampleclass:
	var1 = 'This is var one'
	var2 = 'This is var two'

	def __init__(self, name):
		print "I am in constructor"
		self.name = name


'''
	def set_name(self, name):	#Setter
		self.name = name  		#old style now uses constructor as above
'''
	def get_name(self):   		#Getter
		return self.name

	def class_method(self):
		print "I am in class method"
		print "class method name", self.name

class_obj1 = exampleclass("Rohit")
class_obj2 = exampleclass("XYZ")

print class_obj1.var1
print class_obj2.var2

print class_obj1.get_name()
print class_obj2.get_name()

class_obj1.class_method()
class_obj2.class_method()