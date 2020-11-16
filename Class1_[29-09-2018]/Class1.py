# check type of variable
num1 = 10
num2 = 12.45
num3 = 3 + 4j
print(type(num1))
print(type(num2))
print(type(num3))

a = 1
b = 3.4
a = str(a)
# type casting
print(int(b))
print(a)

# check type by two ways
print(isinstance(2, int))
print("a's value is", a, type(a) is int)

# operation on numbers
print(10 + 2)
print(10 ** 2)  # raised to ^

# python strings
name = "ROHIT"
print('*' * 20)  # operator * is overloaded here
# ,(comma) is adding a space
print('*' * 20, "\n" + name + "\n", '*' * 20)

# string indexing
print(name[0])
print(name[1])
print(name[-1])  # last character
# string slicing
'''
Syntax
string[startindex:stopindex:step]
'''
print(name[2:4])  # index 2 & 3 not 4
print(name[2:4:2])
print(name[:2])  # start from 0th index till 1st index
print(name[2:])  # till end
print(name[::3])  # stepping to every 3rd character
print(name[::])  # prrints all string
# print string in REVERSE by stepping by -1
print(name[::-1])
print("Hello" + name)  # String concatenation

# string Formatting
name, age = 'Ethans', 2
print("{name} is my country of {age} years old".format(name=name, age=age))  # python 3
print(f"Hello {name} age is {age}")  # python 3.6+
# print("%s is my country of %d years old") %('INDIA', 70) #python 2

print(r"\new")  # RAW string does not interpret any characters inside the strings like \n newline etc
