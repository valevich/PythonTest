import sys

# count the arguments
arguments = len(sys.argv) - 1

# output argument-wise
position = 1
while (arguments >= position):
    print ("parameter %i: %s" % (position, sys.argv[position]))
    x = (sys.argv[position])
    print x
    position = position + 1