#Zip() aggregates elements based on the iterables passed, and returns an iterator of tuples
#List of tuples

lt1 = [1,2,3,4,5]
lt2 = ['one','two','three']
lt3 = ['a','b','c','d']

ret = zip(lt1,lt3,lt2)
print ret #will print the list with smallest no. of elements(here lt2)

print "ret[0]",ret[0]

print "type(ret)",type(ret)
print "type(ret[0])",type(ret[0])

#zip(*xyz) -> unzip

print zip(*ret)

l1,l2,l3 = zip(*ret)

print list(l1),l2,l3

#converting lists to dictionary
keys = ['a','b','c']
values = [1,2,3]

d = dict(zip(keys,values))

print d