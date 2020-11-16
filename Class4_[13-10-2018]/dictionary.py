#Dictionary is a collection which is unordered, changeable and indexed
data = { 'name' : 'Rohit',
		 'roll_no' : 20, #will be overriden by last key value
		 'city' : 'Pune',
		 'roll_no' : 34,
		 2 : 234}
#dict() is a constructor too
print data
print "type(data)", type(data)

data['name'] = 'India'
data['call'] = 12345
print data

my_dict = dict(apple="green",banana="yellow",cherry='red') #using dict constructor to make a dictionary or convert to dictionary
print 'my_dict',my_dict

del(my_dict['apple']) #Delete key from dictionary
print "Delete apple", my_dict
print"----------------------------------------------------------------------------------"
print "keys in data:", data.keys()
print "Values in data:", data.values()
print "items in data:", data.items() #returns list of tuples of each key value pair
print "has_key \'cherry\': ", data.has_key('city')
print "get value of key \'name\': ", data.get('name')
print "get value of key \'n\': ", data.get('n') #data['n'] returns error if key doesnot exists, but get() will return none if key doesn't exists

squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print "squares.pop(4):",squares.pop(4) #delete deletes the key/value pair silently where pop returns value while deleting
print "squares", squares
squares[4]=16
print "squares[4]=16",squares
print "squares.popitem()", squares.popitem() #popitem() does not require key like pop(). it pops single key/value pair from start
print squares
print "squares.popitem()", squares.popitem()
print squares
print "squares:",squares.clear() #clears the dictionary

sq = squares #creates reference/alias to squares. Change in sq will reflect in squares.

sq[6] = 36

print "squares",squares
squares.copy() #copy() will create a new copy unlike aliases sq=squares

print 23 in squares
print 6 in squares
print squares.has_key(6)
print len(sq)
sq[7] = ''
print squares

dict1 = {'Name':'Zara','Age':20}
dict2 = {'sex':'female'}

dict1.update(dict2) #update is like extend in lists unlike append() it extends the dictionary
print "dict1",dict1
print "-------------------------------------------------------------------------"





