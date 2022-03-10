from array import *

vals = array('i',[5,6,7,-8,2])

newarr = array(vals.typecode , ( a*a for a in vals ))
print( newarr[2] )
print(vals)
print(vals.buffer_info())
print(vals.reverse())
print(vals)