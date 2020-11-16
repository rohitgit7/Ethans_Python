'''
Write a Python script to ask a key and value from user and add it to a dictionary.

Write a Python script to concatenate following dictionaries to create a new one
dic1={'a':101, 'b':201} 
dic2={'c':301, 'd':401} 
dic3={'e':501, 'f':601}

Write a Python script to check if a given key already exists in a dictionary

WAP to print all the keys of dict

WAP to print TRUE or FALSE based on if key given by user exists in precreated dict

Write a Python program to sum all the values in a dictionary

Write a Python program to remove a key from a dictionary. 

Write a Python program to get the maximum and minimum value in a dictionary

Write a Python program to remove duplicate values from Dictionary

Write a Python program to check a dictionary is empty or not and TRUE or FALSE

Write a Python program to print all unique values in a dictionary

Write a Python program to find the highest 3 values in a dictionary
'''

kv = raw_input("Enter key value pair:")
di = {kv.split(' ')[0]:kv.split(' ')[1]}
print di

dic1={'a':101, 'b':201} 
dic2={'c':301, 'd':401} 
dic3={'e':501, 'f':601}

dic1.update(dic2)
dic1.update(dic3)
print "Concanated dictionaries:",dic1

key = raw_input("Enter key:")
if dic1.has_key(key):
	print "dic1 has a key %s" %key
else:
	print "dic1 does not have key %s" %key

print "All keys of dic1:", dic1.keys()

values = dic1.values()
sum = 0
for n in values:
	sum += n
print "Sum of dic values",sum

del dic1[key]
print "Dictionary after deleting key", dic1

values.sort()
print "Maximum value: %d Minimum value: %d" %(values[-1],values[-0])

result = {}
for key,value in dic1.items():
    if value not in result.values():
        result[key] = value
print result

dic = {}
if len(dic) == 0:
	print "Dictionary is empty"
else:
	print "Dictionary is not empty"

print "Dictionary empty or not:", bool(dic)


dd = {'a': 101, 'c': 201, 'b': 201, 'e': 501, 'f': 601, 'd':501} 
print "Unique values in dd:", set(dd.values())

print "Highest 3 values",values[-3:]