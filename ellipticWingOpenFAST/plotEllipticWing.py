import matplotlib
matplotlib.use('AGG')
import fast_io
import numpy as np
import sys, os, palettable
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

maxTol = 1e-10;
try:
    d1, i1 = fast_io.load_binary_output(sys.argv[1])
except:
    print "Problem reading file ", sys.argv[1]
    
nTimesteps = np.size(d1,0)
nCols = np.size(d1,1)

in_b1Alpha = np.zeros(9)
in_b2Alpha = np.zeros(9)
in_b1Fx = np.zeros(9)
in_b2Fx = np.zeros(9)
in_b1Fy = np.zeros(9)
in_b2Fy = np.zeros(9)

spanLoc = np.array([0.0, 7.23529411765, 14.4705882353, 21.7058823529, 28.9411764706, 39.7941176471, 47.0294117647, 54.2647058824, 61.5])
b1Alpha = np.zeros((9,nTimesteps))
b2Alpha = np.zeros((9,nTimesteps))
b1Fx = np.zeros((9,nTimesteps))
b2Fx = np.zeros((9,nTimesteps))
b1Fy = np.zeros((9,nTimesteps))
b2Fy = np.zeros((9,nTimesteps))

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

def plotAlpha():

    for i in range(0,nTimesteps,100):
        fig = plt.figure()
        ax = plt.axes([0,0,1,1])
        ax.set_color_cycle(palettable.colorbrewer.qualitative.Dark2_8.mpl_colors)
        plt.plot(spanLoc,b1Alpha[:,i])
        plt.xlabel('Span location (m)')
        plt.ylabel('Blade 1 Alpha (degrees)')
        make_axes_area_auto_adjustable(ax)
        plt.savefig('B1Alpha_t{}.png'.format(i))
        plt.close(fig)

def plotFx():

    for i in range(0,nTimesteps,100):
        fig = plt.figure()
        ax = plt.axes([0,0,1,1])
        ax.set_color_cycle(palettable.colorbrewer.qualitative.Dark2_8.mpl_colors)
        plt.plot(spanLoc,b1Fx[:,i])
        plt.xlabel('Span location (m)')
        plt.ylabel('Blade 1 - Tangential force (N)')
        make_axes_area_auto_adjustable(ax)
        plt.savefig('B1Fx_t{}.png'.format(i))
        plt.close(fig)

def plotFy():

    for i in range(0,nTimesteps,100):
        fig = plt.figure()
        ax = plt.axes([0,0,1,1])
        ax.set_color_cycle(palettable.colorbrewer.qualitative.Dark2_8.mpl_colors)
        plt.plot(spanLoc,b1Fy[:,i])
        plt.xlabel('Span location (m)')
        plt.ylabel('Blade 1 - Normal force (N)')
        make_axes_area_auto_adjustable(ax)
        plt.savefig('B1Fy_t{}.png'.format(i))
        plt.close(fig)

if __name__=="__main__":
    
    plotAlpha()
    plotFx()
    plotFy()
    
    

        
        
