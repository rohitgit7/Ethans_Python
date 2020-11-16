#Enumerate() method adds a counter

lt1 = ["India","Pakistan","Australia"]

en = enumerate(lt1)

print lt1
print en
print type(en)

print list(en)
print list(en) #why blank? enumerator uses generator, we can use en.next()

en1 = enumerate(lt1,4) #start counter from 4
print "list(en1)",list(en1)

for count, value in enumerate(lt1):	#Enumerate return two values counter and list element
	print (count,value)		#prints tupels

print count


