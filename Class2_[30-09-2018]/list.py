my_list = ["apple","banana","cherry"]
print my_list[0]
my_list[0] = 'test'
print my_list
#my_list[5] = 'a' # will give an error

#list slicing is same as string [::]

my_list.append("banana") #append does not return anything
my_list.append("banana")
print my_list
my_list.remove("banana") #Remove also does not return anything
print my_list
print "Lenth of my_list is:",len(my_list)
print "Count of banana is:", my_list.count("banana") #count is used to count perticular object unlike length where all objects are counted
print "Cherry's index is:",my_list.index("cherry")

list1=[2,3,4]
list2=[7,8,9]
print list1,list2

list1.append(list2) #append takes complete string/list as single element
print list1

list1.extend(list2) #extend adds elements separately
print list1
print list1[3][1]

list1.insert(6,'India') #inserts element in the list at specified index
print list1
print list1.pop(3) #returns and removes element at specified index
print list1

list1.reverse()
print "list in reverse",list1
list1.sort()
print "sorted list1",list1	
	

a=[1,2,3,4,5]
b=[1,2,3,'',4]

print "any a",any(a) #(Boolean)checks if atleast one element is true i.e. not-blank
print "any b",any(b) 
print "all a",all(a) #(Boolean)checks if all the elements are true
print "all b",all(b)

#Nested list
c=[a,b]
print "print c",c
print "c[0][3]",c[0][3]

#Range function
#range(start,stop,step)
print range(10) #0 to 9
print range(4,10) #4 to 9
print range(4,20,3) #4 to 20 stepping every 3 digit




