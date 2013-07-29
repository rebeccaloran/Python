# -*- coding: utf-8 -*-
# File: ex6.py
# Description:
#
# prints the string
print "Mary had a little lamb."
# prints the string, with 'snow' referenced by [ %s ]
print "Its fleece was white as %s." % 'snow'

# prints the string
print "And everywhere that Mary went."
# prints `.' 10 times
print "." * 10 # what'd that do?

# assigns the string `C' to [ end1 ] 
end1 = "C"
# assigns the string `h' to [ end2 ]
end2 = "h"
# assigns the string `e' to [ end3 ]
end3 = "e"
# assigns the string `e' to [ end4 ]
end4 = "e"
# assigns the string `s' to [ end5 ]
end5 = "s"
# assigns the string `e' to [ end6 ] 
end6 = "e"
# assigns the string `B' to [ end7 ]
end7 = "B"
# assigns the string `u' to [ end8 ]
end8 = "u"
# assigns the string `r' to [ end9 ]
end9 = "r"
# assigns the string `g' to [ end10 ]
end10 = "g"
# assigns the string `e' to [ end11 ]
end11 = "e"
# assigns the string `r' to [ end12 ]
end12 = "r"

# watch what comes in the end. try removing it to see what happens
# Prints [ end6 ] concantenated after [ end1 ... end5 ] 
print end1 + end2 + end3 + end4 + end5 + end6, # prevents newline
# Prints [ end12 ] concantenated after [ end7 ... end11 ]
print end7 + end8 + end9 + end10 + end11 + end12 

