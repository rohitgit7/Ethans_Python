import mod1 #It looks for module in local directory first
import os,sys #can call multiple modules with comma separated

from mod1 import string #call only single data structure from particular module. We can also call string directly without writing mod1.string
from mod1 import * # it is not recommended as it brings everything to local namespace

from mod1 import string as new, func1 as f1 #assigning a new reference to the object
import mod1 as new_mod  #when we need to call same module with different name

#print string	#it is working   because we have used from mod1 import string
print mod1.lt
mod1.func1("Hello")

print mod1.__file__	#prints the location of the module called
f1("func1 as f1")

lt = [1,2,3,4]

print dir()	#view current namespace
print dir(mod1) #view namespace in mod1
print dir(lt) #view all functions for lt(list) data structure

reload(mod1) #if we have modified a called module and it has already been called then we can reload it(Mostly used in interactive shell)