from openseespy.opensees import *
import math
import sys

#limpia el modelos
wipe()

#defino el tipo de modelo
model('basic','-ndm',3,'-ndf',6)

M = 0.

massType = "-lMass"  # -lMass, -cMass
coordTransf = "Linear"  # Linear, PDelta, Corotational

#creo los nodos
node(1,0.0,0.0,0.0)
node(2,10.0,0.0,0.0)
node(3,0.0,0.0,10.0)
node(4,10.0,0.0,10.0)
node(5,0.0,10.0,0.0)
node(6,10.0,10.0,0.0)
node(7,0.0,10.0,10.0)
node(8,10.0,0.0,10.0)


#fijo los nodos de abajo
vals = [1,1,1]

fix(1,1,1,1,1,1,1)
fix(2,1,1,1,1,1,1)
fix(3,1,1,1,1,1,1)
fix(4,1,1,1,1,1,1)

#materiales
A = 40.0
E = 50000.0
I = A*A*A*A
print(I)

#creo los elementos

geomTransf(coordTransf, 1, 1.0, 0.0, 0.0)


element('elasticBeamColumn',1,1,5,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',2,2,6,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',3,3,7,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',4,4,8,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',5,5,7,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',6,6,8,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',7,5,6,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)
element('elasticBeamColumn',8,7,8,A,E,20000.0,20000.0,I,I,1,'-mass', M, massType)

timeSeries('Linear',1)

pattern('Plain',1,1)

load(5,0,500,0,0,0,0)

system('BandSPD')

numberer('RCM')

constraints('Plain')

integrator('LoadControl',1.0)

algorithm('Linear')

analysis('Static')

analyze(1)

printModel()




