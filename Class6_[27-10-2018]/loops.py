i = 0
while i < 11:
	print i
	i += 1
else:	#else will execute after executing while block and condition fails
	print "i is greater than 10"

for char in 'PYTHON':
	print char

num = [1,2,3,4]
for n in num:
	print n, #(,)comma removes newline character

num = [(1,2),(2,3),(4,5)]
for n,n1 in num:
	print n	
	print n1,

#Loop keywords
#break -> break the loop, do not execute again.
#continue -> continue will not excute the code beyond the continue word till end of loop and will go back to loop
#pass -> it will not do anythin just moves ahead

lt = range(1,8)
for num in lt:
	print "inside the loop : %s", num
	if num < 5:
		print "number:%s", num
	elif num == 5:
		continue
	elif num > 5 and num < 8:
		pass
	else:
		break
	print "[%s]i m outside the conditions", num