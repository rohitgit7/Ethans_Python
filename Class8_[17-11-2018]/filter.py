#Filter creates a list of elements for which a function returns TRUE
#Return only TRUE values or non-zero values

num_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0, num_list))

print num_list
print less_than_zero
