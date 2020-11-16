#Any python file .py is a module. to call that file just write "import <filename without .py>"
#set PYTHONPATH

string = "India is my country"

if __name__ == "__main__": #The code in this module will be executed as standalone for unit testing. It will not be executed when it is called in another module, here call_mod1.py
	print string

lt = [1,2,3,4]

def func1(arg):
	print arg

if __name__ == '__main__':
	func1("__main__")