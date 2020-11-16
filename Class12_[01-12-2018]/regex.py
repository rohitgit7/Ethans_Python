import re

#match() checks for a match only at the beginning of the string
#while search() checks for a match anywhere in the string

var = "This is a regex with is repeated"
a = re.match(r'(.*) is (.*)',var)
s = re.search(r'(.*) is (.*)',var)
print a
print a.group()
print a.group(1)
print a.group(2)

print s.group()
print s.group(1)

line = "THIS IS CAPS STRING"
b = re.match(r'T.*is.*',line,re.I)
print b
print b.group()

phone = "123-456-789 # This is phone number"
num = re.sub(r'\D',"",phone)
print num
num1 = re.sub(r'#.*$',"",phone)
print num1

#re.findall()