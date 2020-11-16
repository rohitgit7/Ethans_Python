#0 = False
#non-zero are True

name1 = raw_input("Enter name1:")
name2 = raw_input("Enter name2:")
if name1 != name2:
	print "Names are not same"
elif name1=='Rohit':
	print "Name is Rohit"
else:
	print "Names are same"

stud = {1:{'Name':'Prakash','boy':True,'girl':False},
		2:{'Name':'Pooja','boy':False,'girl':True}}
sname = 'Pooja'
if stud[1]['girl']:
	print "Roll no. 1 is a girl"
elif stud[1]['boy']:
	print "Roll no. 1 is boy"
elif stud[2]['boy']:
	print "Roll no. 2 is boy"
elif stud[2]['girl']:
	print "Roll no. 2 is girl"
else:
	print "Unidentified!"

# logical operator - and, or, not