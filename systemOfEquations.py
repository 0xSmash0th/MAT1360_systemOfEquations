#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#set your figure scale here
gridSize = 10
stride=1
granularity = 1 # .1 is possible but slow
def getPlot(a, b, c, d):
	""" 	
	a plane is a*x+b*y+c*z+d=0
	[a,b,c] is the normal. Thus, we have to calculate
	d and we're set 
	"""
	normal = np.array([a,b,c])
	print "normal", normal
	if a != 0:
		x = (1.*d)/a
		point = np.array([x,0,0])
	elif b != 0:
		x = (1.*d)/b
		point = np.array([0,x,0])
	elif c != 0:
		x = (1.*d)/c
		point = np.array([0,0,x])
	else:
		print "Bail! a, b and c must not all be zero"
		sys.exit(1)
	
	print "point", point
	d = -np.sum(point*normal)# dot product
	# create x,y
	x = np.arange(-1 * gridSize, gridSize, granularity)
	y = np.arange(-1 * gridSize, gridSize, granularity)
	xx, yy = np.meshgrid(x, y, sparse=True)
	# calculate corresponding z
	z = (-normal[0]*xx - normal[1]*yy - d)*1./normal[2]
	return xx, yy, z

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.set_xlabel('x axis')
plt3d.set_ylabel('y axis')
plt3d.set_zlabel('z axis')

# enter getPlot(a, b, c, d)
# e.g 7x + 16y + 6z = 17
# x, y, z = getPlot (7, 16, 6 -17)
"""
#one intersect
x, y, z = getPlot(4, 6, 5, 13)
plt3d.plot_surface(x,y,z, color='blue', rstride=stride, cstride=stride)
x, y, z = getPlot(5, -3, -6, 11)
plt3d.plot_surface(x,y,z, color='yellow', rstride=stride, cstride=stride)
x, y, z = getPlot(1, 1, -1, -2)
plt3d.plot_surface(x,y,z, color='cyan', rstride=stride, cstride=stride)
"""

"""
#no intersect
x, y, z = getPlot(7, 16, 6, -17)
plt3d.plot_surface(x,y,z, color='blue', rstride=stride, cstride=stride)
x, y, z = getPlot(3, 7, 5, 2)
plt3d.plot_surface(x,y,z, color='yellow', rstride=stride, cstride=stride)
x, y, z = getPlot(1, 2, -4, -4)
plt3d.plot_surface(x,y,z, color='cyan', rstride=stride, cstride=stride)
"""

# infinitely many 
x, y, z = getPlot(3, 9, -13, 1)
plt3d.plot_surface(x,y,z, color='blue', rstride=stride, cstride=stride)
x, y, z = getPlot(4, 11, -16, -4)
plt3d.plot_surface(x,y,z, color='yellow', rstride=stride, cstride=stride)
x, y, z = getPlot(1, 2, -3, -3)
plt3d.plot_surface(x,y,z, color='cyan', rstride=stride, cstride=stride)

plt.show()
