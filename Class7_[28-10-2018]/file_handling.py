#File handling
#If buffer set to '0' then no buffering will take place, if it is set to any integer(1,2,...n) then those many lines will get buffered
#access modes read, write, append
#it reads files from OS filestream
#Modes - "r","a","w","r+","w+" - Default mode is "r"
#r+ will give error if file does not exists
#w+ will create file if file does not exists

path = r"E:\Programs\Python\SublimeText\Class3_[06-10-2018]\Exercise.txt"  #'r' is for raw string, it does not interpret any special character

fh = open(path,"r")

fh1 = open(path,"r",5) #buffer of 5 lines

print "Mode:", fh.mode
print "File name:", fh.name
print "File closed or not:", fh.closed

fh1.close() #will close the file and writes the chnanges to the file

#print fh.read() #reads whole file
print fh.read(5) #reda 5 bytes from file

fh.close()

path1 = r"E:\Programs\Python\SublimeText\Class7_[28-10-2018]\file.txt"
f = open(path1,"w+")

f.write("This is a first line in a file.txt")
f.flush() #explicitly flush the contents to the file
print "Tell:",f.tell() #due to writing the file pointer will be at the end of file
f.seek(0) #In order to read the file we need to point it to start of the file
print f.read()
f.close()

f1 = open(path1,"r")
print f1.read()
print f1.tell() #current position of pointer
print f1.read() #will return blank as the current pointer is at end of the file
f1.seek(0) #will move pointer at the beginning of the file
print f1.read()

#with statement -> any file opned will be closed automatically after you are done

