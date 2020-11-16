#result = [*transform* *iteration* *filter*]

x = [i for i in range(10)]

print x

squares = [x**2 for x in range(10)]
print squares

multiplied = [item*3 for item in squares]
print multiplied

#WAP to create list of first letter of list2 in upper case
lt1 = [a.title() for a in 'india','america','pakistan']
print lt1

string = "Hello 12345 World"
num = [int(x) for x in string if x.isdigit()] #isdigit() will return only numbers
print num
print type(num[0])

print [x+y for x in [10,30,50] for y in [20,40,60]] #nested for loop
