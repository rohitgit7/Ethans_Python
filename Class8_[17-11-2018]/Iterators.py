#Generators run on the fly

lt1 = [x*x for x in range(5)]
print "type(lt1)",type(lt1)
print lt1
print "len(lt1)",len(lt1)

gen1 = (x*x for x in range(5))
print "type(gen1)",type(gen1) #() gives type as generator
print gen1 #print object location
#print "len(gen1)",len(gen1) #Throws error because there is no length to generators as it runs on the fly

print gen1.next()
print gen1.next()
print "************"
for i in gen1:
	print i

#print gen1.next() #Throws StopIterationError as there are no more elements to generate, logic ends

def find_even_number_function(num_stream):
	even_num = []
	for n in num_stream:
		if n % 2 == 0:
			even_num.append(n)
	return even_num

a = find_even_number_function([1,2,3,4,5,6,7])
print "type(a)",type(a)
print a

#Yield returns generator in function unlike return who returns result

def find_even_number_generator(num_stream):
	for n in num_stream:
		if n % 2 == 0:
			yield n

b = find_even_number_generator([1,2,3,4,5,6,7,8,9])
print "type(b)",type(b)
print b.next()

#range vs xrange
#range() returns a list of numbers created using range() function
#xrange() returns a generator object

print "**xrange**"
a = xrange(5)
print a[3]

for i in a:
	print i

