
##################################################################
## 3D frame example to show how to render opensees model and 
## plot mode shapes
##
## By - Anurag Upadhyay, PhD Candidate, University of Utah.
## Date - 12/01/2019
##################################################################

from openseespy.postprocessing import * 
import openseespy.postprocessing
from openseespy.opensees import *
import openseespy
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from math import asin, sqrt


# set some properties
wipe()

model('Basic', '-ndm', 3, '-ndf', 6)

# properties
# units kip, ft

numBayX = 2
numBayY = 2
numFloor = 7

bayWidthX = 120.0
bayWidthY = 120.0
storyHeights = [162.0, 162.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0]

E = 29500.0
massX = 0.49
M = 0.
coordTransf = "Linear"  # Linear, PDelta, Corotational
massType = "-lMass"  # -lMass, -cMass

nodeTag = 1

# add the nodes
#  - floor at a time
zLoc = 0.
for k in range(0, numFloor + 1):
	xLoc = 0. 
	for i in range(0, numBayX + 1):
		yLoc = 0.
		for j in range(0, numBayY + 1):
			node(nodeTag, xLoc, yLoc, zLoc)
			mass(nodeTag, massX, massX, 0.01, 1.0e-10, 1.0e-10, 1.0e-10)
			if k == 0:
				fix(nodeTag, 1, 1, 1, 1, 1, 1)
				
			yLoc += bayWidthY
			nodeTag += 1
			
		xLoc += bayWidthX

	if k < numFloor:
		storyHeight = storyHeights[k]
	
	zLoc += storyHeight

	print(xLoc,yLoc,zLoc)

# add column element
geomTransf(coordTransf, 1, 1, 0, 0)
geomTransf(coordTransf, 2, 0, 0, 1)

eleTag = 1
nodeTag1 = 1
nodos1 =[]
nodos2 = []
nodosTotal=[]
elementos = []

for k in range(0, numFloor):
	for i in range(0, numBayX+1):
		for j in range(0, numBayY+1):
			nodeTag2 = nodeTag1 + (numBayX+1)*(numBayY+1)
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 1, '-mass', M, massType)
			eleTag += 1
			nodeTag1 += 1


nodeTag1 = 1+ (numBayX+1)*(numBayY+1)
#add beam elements
for j in range(1, numFloor + 1):
	for i in range(0, numBayX):
		for k in range(0, numBayY+1):
			nodeTag2 = nodeTag1 + (numBayY+1)
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 2, '-mass', M, massType)
			eleTag += 1
			elementos.append(eleTag)

			nodeTag1 += 1
		
	nodeTag1 += (numBayY+1)


nodeTag1 = 1+ (numBayX+1)*(numBayY+1)
#add beam elements
for j in range(1, numFloor + 1):
	for i in range(0, numBayY+1):
		for k in range(0, numBayX):
			nodeTag2 = nodeTag1 + 1
			nodos2.append(nodeTag2)
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 2, '-mass', M, massType)
			eleTag += 1
			elementos.append(eleTag)
			nodeTag1 += 1
		nodeTag1 += 1
		nodos1.append(nodeTag1)

elementos.sort()
for item in nodos1:		
	nodosTotal.append(item)
for item in nodos2:
	nodosTotal.append(item)	
nodosTotal.sort()

# calculate eigenvalues & print results
numEigen = 7
eigenValues = eigen(numEigen)
print(eigenValues)
PI = 2 * asin(1.0)



#
# print(nodosTotal)
for item in elementos:
	print('elemento ',item,"-->", basicDeformation(item))

# plot_modeshape(5)
# plot_model()
# # plot_modeshape(2)
# # plot_model()
