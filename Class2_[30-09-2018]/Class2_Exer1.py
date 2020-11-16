Name = raw_input('Enter your name: ')
Age = int(raw_input('Enter your age: '))
year = (2018 - Age) + 100
name = Name.split(' ')
#name.split(' ')[0].upper()
#name.split(' ')[1].lower()
print "Hello", name[0].upper(), name[1].lower()
print "You will turn 100 in year", year
