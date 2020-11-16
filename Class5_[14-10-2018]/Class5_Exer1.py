#Dictionary of dictionary(Nested dictionary)

dict1 = {1:1,2:4,3:9}
dict2 = {'a':dict1[1]}
dict2['b'] = dict1[2]

dict3 = {'a':{1:1,2:4}}

print "dict2",dict2
print "dict3",dict3
print "dict3['a'][2]->",dict3['a'][2]

#Dictionary of list
lt1 = range(4,7)
print "list", lt1
dictoflist = {'a':lt1}
print "dictoflist",dictoflist
print "dictoflist['a'][2]->",dictoflist['a'][2]

#list of dictionary
lt2 = [dict1,dict2,dict3]
print "list of dictionary",lt2
print "lt2[2]['a'][2]=>",lt2[2]['a'][2]

#list of list
lt2.append(lt1)
print "list of list", lt2
print "lt2[3][2]=>",lt2[3][1]