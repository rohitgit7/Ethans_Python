a = 10
b = 15 
#Operators
print "a and b", a , b
print "a==b",a==b
print "a>b",a>b
print "a<b",a<b
print "a<=b",a<=b
print "a!=b",a!=b
print "a<>b",a<>b

#Membership operators
#in
#not in
lt = range(5)
print lt
print "5 in lt->",5 in lt
print "5 not in lt->",5 not in lt
print "3 in lt->",3 in lt

string = "This is a string"
print "is in string=>",'is' in string

#Identity operators
#is
#not is
#id()

a = 20
b = 20
print "a is b=>", a is b
a += 1
print "a is b=>", a is b
l1 = range(1,5)
l2 = range(1,5)
print id(l1),id(l2)
print "l1 is l2=>", l1 is l2
