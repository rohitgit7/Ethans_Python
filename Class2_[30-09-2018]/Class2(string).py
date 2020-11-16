# String function
name = "  Hello World! "
print(name)
print(name.strip())  #removes spaces from beginning and end
print(name.lower()) #convert string lower case
print(name.upper()) #convert string to upper case

print(len(name))  # Global function to count the length of value

greet = "Good Morning! Morning morning"
print(greet)
print(greet.replace('Morning','Night')) #Replaces first word with second one
print(greet.split('!')) #Splits the Sting from delimiter

#input = raw_input('Enter your name: ') #Python 2.7
input = input('Enter your name: ') #Python 3+
