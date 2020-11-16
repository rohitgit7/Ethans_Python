#Set is a collection which is unordered and unindexed

myset = {"apple","banana","cherry"}
print "myset",myset
myset1 = set(("apple","banana","cherry")) #converting tuple to set
print "type of myset1",type(myset1)

myset.add("pear")
print "pear added",myset
myset.remove("banana")
print "removed banana",myset
print "length of myset",len(myset)

myset.add("pear")
print myset

list1 = [1,2,3,4]
#myset.add(list1) #Not allowed, because list is indexed

list2 = [1,1,1,2,3,3,3,3,2,2,4,4,4]
print "list2", set(list2)

print "------------------------------------------------"

managers = set(('Akash','Rahul','Rohit'))
print "managers",managers
engineers = set(('Rohit',)) #if single element in tuple then add comma(,) at the end
print "engineers",engineers

print managers & engineers #Intersection
print managers - engineers #Compliment
print managers | engineers #Union