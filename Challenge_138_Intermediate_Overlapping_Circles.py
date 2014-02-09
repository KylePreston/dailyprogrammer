# My solution to /r/dailyprogrammer
# Goal is to write a program that takes two unit-circles (radius of one) at given locations
# and compute that shape's volume. You must make sure to not double-count the intersecting volume!
# (i.e. you must not sum this red area twice). 


# Assuming unit circles

from math import acos, pi, sqrt

def circle_area(x1, y1, x2, y2):

	# pythagorean theorem
	dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

	# http://mathworld.wolfram.com/Circle-CircleIntersection.html
	if dist >= 2:
		return 2 * pi
	else:
		return (2 * pi) - ((2 * acos(dist/2)) + (dist/2) * sqrt(4 - dist ** 2))

inputs = []

for i in range(4):
	cord = int(raw_input('Enter coordinate #%d: ' % (i + 1)))
	inputs.append(cord)

print ("Total area: "),
print (circle_area(inputs.pop(), inputs.pop(), inputs.pop(), inputs.pop()))
