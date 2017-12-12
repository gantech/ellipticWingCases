import matplotlib
matplotlib.use('AGG')
import fast_io
import numpy as np
import sys, os, palettable
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

maxTol = 1e-10;
try:
    d1, i1 = fast_io.load_ascii_output('/Users/gvijaya/CurrentProjects/HFM/FSI/11_2017/ellipticWing/ellipticWingCases/p1/deltaOverC_0p25/EllipticWing.T1.out')
except:
    print "Problem reading file EllipticWing.T1.out"

# Elliptic wing details    
c0 = 1.0 # max chord
b = 10.0 # span
area = np.pi * 0.25 * c0 * b
spanLoc = np.array([0.0, 1.17647058824, 2.35294117647, 3.52941176471, 4.70588235294, 6.47058823529, 7.64705882353, 8.82352941176, 10.0])

#Simulation details
dt = 0.0025
aoa = 7.0 * np.pi / 180.0
uInfty = 10.0
rho = 1.225 
dynPres = 0.5 * rho * uInfty * uInfty

nTimesteps = np.size(d1,0)
nCols = np.size(d1,1)

in_b1Alpha = np.zeros(9)
in_b2Alpha = np.zeros(9)
in_b1Fx = np.zeros(9)
in_b2Fx = np.zeros(9)
in_b1Fy = np.zeros(9)
in_b2Fy = np.zeros(9)

b1Alpha = np.zeros((9,nTimesteps))
b2Alpha = np.zeros((9,nTimesteps))
b1Fx = np.zeros((9,nTimesteps))
b2Fx = np.zeros((9,nTimesteps))
b1Fy = np.zeros((9,nTimesteps))
b2Fy = np.zeros((9,nTimesteps))

RtAeroFxh = np.zeros(nTimesteps)
RtAeroFyh = np.zeros(nTimesteps)
RtAeroFzh = np.zeros(nTimesteps)

for n in range(9):
    for j in range(nCols):
        if 'B1N{}Alpha'.format(n+1) in i1['attribute_names'][j]:
            in_b1Alpha[n] = j
            b1Alpha[n,:] = d1[:,j]
        if 'B1N{}Fx'.format(n+1) in i1['attribute_names'][j]:
            in_b1Fx[n] = j
            b1Fx[n,:] = d1[:,j]
        if 'B1N{}Fy'.format(n+1) in i1['attribute_names'][j]:
            in_b1Fy[n] = j
            b1Fy[n,:] = d1[:,j]
        if 'RtAeroFxh' in i1['attribute_names'][j]:
            RtAeroFxh = d1[:,j]
        if 'RtAeroFyh' in i1['attribute_names'][j]:
            RtAeroFyh = d1[:,j]
        if 'RtAeroFzh' in i1['attribute_names'][j]:
            RtAeroFzh = d1[:,j]

aoaDistrib = b1Alpha[:,-1]
lfpul = b1Fy[:,-1]
dfpul = b1Fx[:,-1]
TotLiftCoeff = -RtAeroFyh / (dynPres * area)
TotDragCoeff = RtAeroFxh / (dynPres * area)

#Actuator data
act_x, act_y, act_z, act_fx, act_fy, act_fz = np.loadtxt('/Users/gvijaya/CurrentProjects/HFM/FSI/11_2017/ellipticWing/ellipticWingCases/p1/deltaOverC_0p25/actuator_forces.csv',delimiter=',',unpack=True)
act_x, act_y, act_z, act_vx, act_vy, act_vz = np.loadtxt('/Users/gvijaya/CurrentProjects/HFM/FSI/11_2017/ellipticWing/ellipticWingCases/p1/deltaOverC_0p25/actuator_velocity.csv',delimiter=',',unpack=True)
act_span = -act_y[1:51] - 1.5
act_lift = -act_fz[1:51]
act_drag = act_fx[1:51]
vec_atan = np.vectorize(np.arctan)
act_aoa = 7.0 - vec_atan(act_vz[1:51]/act_vx[1:51])*180.0/np.pi
 
