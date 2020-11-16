class parent1:
	firstvar = "This is firstvar in parent1"
	secondvar = "This is secondvar in parent1"

class parent2(object):				#object is passed means it inherits ONLY object class nothing else
	thirdvar = "This is thirdvar in parent2"
	secondvar = "This is second var in parent2"

class child(parent2,parent1):  #secondvar is in both parents, so it will check left to right first self Child class then parent2 then parent1
	pass

child_obj = child()

print child_obj.firstvar
print child_obj.secondvar


#### Setting attributes to instance

print hasattr(child_obj,'firstvar')   #returns boolean if attribute us present in the instance(child_obj)
print getattr(child_obj,'firstvar')   #returns value of attribute in the instance

setattr(child_obj,'var2','This is var2')  #Sets attribute for instance
print getattr(child_obj,'var2') 

delattr(child_obj,'var2')    #deletes attribute from instance