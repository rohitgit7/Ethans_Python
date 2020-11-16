train_no1 = range(234,242)
itinarary1 = {'a':'Mumbai','b':'Pune','c':'Delhi','d':'Jaipur'}
coaches1 = ["AC","sleeper","first-class","second-class"]
birth_type1 = ["upper","middle","lower"]
seat_no1 = range(23,34)
available_seat1 = [23,33,27,25,32]


train = {
		'trainno':train_no1,
		'stopages':itinarary1,
		'coaches':coaches1,
		'birth':birth_type1,
		'seat':seat_no1,
		'available_seat':available_seat1
		}

print train
dest = train['stopages'].values()
print "dest", dest
ip = raw_input("Enter destination:")
print type(ip), type(dest)
i = 0
while i < 4:
	print "i",i 
	if dest[i] == ip:
		print "Destination available", dest[i]
	i += 1
