#Tuple cannot be modified as list
#Tuple is collection which is ordered and unchangeable(Immutable)
tup1 = (1,2,3)
tup2 = (5,6,7,8)
list1 = [tup1,tup2]
print "printing list",list1

list2 = ['a','b','c']
list3 = ['p','q','r','s']
tup3 = (list2,list3)
print "Printing tuple",tup3

#tup3.append("append") #Will throw an error beacuse tuple are immutable
tup3[0].append("append") #will work because here, we are modifying list inside the tuple
print "Printing tuple",tup3
print "Length of tuple",len(tup3)

