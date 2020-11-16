#raise Exception('This is a generic exception')

#raise MemoryException('xyz')

password = '1234'
if password != '1234':
	raise Exception("Wrong password!")


#AssertionError Exception is used for debugging than throwing runtime exception

platform = 'linux'
a = 'abc'
assert 'linux' in platform, "This code runs on Linux only!"
#assert 'windows' in platform, "This code runs on Linux only!"

assert a.isdigit(), "Only digits are allowed"