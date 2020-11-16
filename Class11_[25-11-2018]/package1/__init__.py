print "This is __init__.py in package1"

global_var = "This is Global var"

import package1.mod1, package2.mod2 #will automatically import package2.mod2 from PYTHONPATH i.e. the path @package1 is located

#__all__ = ['package1.mod1','package2.mod2'] #when calling "from package1 import *" it will import mentioned objects in __all__ list