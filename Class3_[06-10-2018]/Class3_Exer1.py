'''
WAP to take input string from user and print the length of string

Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

Write a Python program to get a single string from two given strings by user , separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'

Write a Python program to change a given string to a new string where all the even position characters are in starting and all odd position characters are in end.

Write a Python program to remove the characters which have odd index values of a given string

WAP to insert a string in the middle of a other string.	
Write a Python program to remove duplicates from a list
Write a Python program to find the length of all words of a list

Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

Write a Python program to generate a 3*4*6 3D array whose each element is *

Write a Python program to get the difference between the two lists.

Write a Python program to find the index of an item in a specified list

Write a Python program to append a list to the second list. 

Write a Python program to get unique values from a list

Write a Python program to count the number of elements in a list within a specified range

Write a Python program to check whether a list contains a sublist

Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''	
ip = raw_input("Enter string:")
print "Length of the string is:", len(ip)
print "First 2 and last 2 characters:", ip[:2] + ip[-2:]
lt = ip.split(" ")
print "First 2 swap:", lt[1][:2] + lt[0][2:] + " " + lt[0][:2] + lt[1][2:]
print "even odd:", ip[1::2] + ip[0:-1:2]
print "odd index remove:", ip[0::2]

print "String in Middle:", ip.split(" ")[0] + " H " + ip.split(" ")[1]

lt1=[2,3,4,3,3,4,4,2,2,5,6,1]
print "List1",lt1
lt1 = set(lt1)
print "remove duplicates", lt1
print "list length:",len(lt[1:])

lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

lst[1:4].extend(lst[6:])
print "0th,4th and 5th", lst