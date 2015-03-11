"""
Version: 1.0
Authors: Gambin Iñigo / Pastor Aznar
Date: 11-03-15
"""

def drink(beer):
 if beer == 0:
  print ""
 else:
  print beer ," bottles of beer on the wall, ", beer ," bottles of beer."
  print "Take one down, pass it around, ", beer-1 ," bottles of beer on the wall.\n"
  drink(beer-1)

drink(100)
