import matplotlib
matplotlib.use('AGG')
from matplotlib.ticker import MaxNLocator
import numpy as np
import sys, os, palettable, importlib, cycler
import matplotlib.pyplot as plt
plt.style.use('twoColumn_legendabove')

colorcycle = cycler.cycler('color',palettable.colorbrewer.qualitative.Dark2_8.mpl_colors)

# Elliptic wing details    
c0 = 1.0 # max chord
b = 10.0 # span
area = np.pi * 0.25 * c0 * b
spanLoc = np.array([0.0, 1.17647058824, 2.35294117647, 3.52941176471, 4.70588235294, 6.47058823529, 7.64705882353, 8.82352941176, 10.0])
chord = np.array([1e-06, 0.644379479418, 0.848365005992, 0.955769224075, 0.998268396969, 0.955769224075, 0.848365005992, 0.644379479418, 1e-06])

#Simulation details
aoa = 7.0 * np.pi / 180.0
uInfty = 10.0
rho = 1.225 
dynPres = 0.5 * rho * uInfty * uInfty
gamma_max = 2.0 * b * uInfty * aoa / (1.0 + 4.0 * b / (2.0 * np.pi * c0))
CL_liftingLine = 0.5 * np.pi * (b / area) * gamma_max / uInfty
CD_liftingLine = (0.25 * np.pi / area) * gamma_max * gamma_max / (uInfty * uInfty)
wi_liftingLine = 0.5 * gamma_max / b
aoa_liftingLine = (aoa  - np.arctan(wi_liftingLine/uInfty)) * 180.0/np.pi
lfpul_liftingLine = 0.5 * rho * (uInfty*uInfty + wi_liftingLine*wi_liftingLine) *  (2.0 * np.pi) * (aoa_liftingLine * np.pi/180.0) * chord * np.cos( np.arctan(wi_liftingLine/uInfty)  )
dfpul_liftingLine = 0.5 * rho * (uInfty*uInfty + wi_liftingLine*wi_liftingLine) *  (2.0 * np.pi) * (aoa_liftingLine * np.pi/180.0) * chord * np.sin( np.arctan(wi_liftingLine/uInfty)  )

p1_caseLabels = {'deltaOverC_0p5':r'$\Delta/c_0 = 0.5$','deltaOverC_0p25':r'$\Delta/c_0 = 0.25$', 'deltaOverC_0p125':r'$\Delta/c_0 = 0.125$', 'deltaOverC_0p25_e0p5':r'$\Delta/c_0 = 0.25, \epsilon = 0.5$', 'deltaOverC_0p125_e0p5':r'$\Delta/c_0 = 0.125, \epsilon = 0.5$'}
p1_cases = ['deltaOverC_0p5','deltaOverC_0p25','deltaOverC_0p125','deltaOverC_0p25_e0p5', 'deltaOverC_0p125_e0p5']
p1_caseData = {}

for i in p1_cases:
    sys.path.append('../p1/{}'.format(i))
    p1_caseData[i] = my_module = importlib.import_module(i)

    with open('{}.txt'.format(i),'w') as f:
        f.write('#spanLoc Lift Drag \n')
        for j in range(np.size(p1_caseData[i].act_span)):
            f.write('{}   {}   {} \n'.format(p1_caseData[i].act_span[j],p1_caseData[i].act_lift[j],p1_caseData[i].act_drag[j]))

def plotActuatorForce():
    """ Plot Actuator force distribution from last time step from all P1 cases """
    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].act_span,p1_caseData[i].act_drag,label=p1_caseLabels[i])
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.xlabel('Span location (m)')
    plt.ylabel('Actuator Drag force (N)')
    plt.tight_layout(rect=[0,0,1,0.8])
    plt.savefig('actuator_drag_force.pdf')
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].act_span,p1_caseData[i].act_lift,label=p1_caseLabels[i])
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.xlabel('Span location (m)')
    plt.ylabel('Actuator Lift force (N)')
    plt.tight_layout(rect=[0,0,1,0.8])
    plt.savefig('actuator_lift_force.pdf')
    plt.close(fig)

def plotActuatorAoA():
    """ Plot Actuator angle of attack distribution from last time step from all P1 cases """
    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].act_span,p1_caseData[i].act_aoa,label=p1_caseLabels[i])
    plt.axhline(aoa_liftingLine,label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.xlabel('Span location (m)')
    plt.ylabel('Angle of attack (degrees)')
    plt.tight_layout(rect=[0,0,1,0.8])
    plt.savefig('actuator_aoa.pdf')
    plt.close(fig)
    
def plotAlpha():
    """ Plot Alpha distribution from last time step from all cases """
    fig,ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].spanLoc,p1_caseData[i].aoaDistrib,label=p1_caseLabels[i])
    plt.plot(spanLoc,aoa_liftingLine*np.ones(np.size(spanLoc)),label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.xlabel('Span location (m)')
    plt.ylabel('Angle of Attack (degrees)')
    plt.tight_layout(rect=[0,0,1,0.8])
    plt.savefig('AoA.pdf')
    plt.close(fig)

def plotDragDistrib():

    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].spanLoc,p1_caseData[i].dfpul,label=p1_caseLabels[i])
    plt.plot(spanLoc,dfpul_liftingLine,label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.xlabel('Span location (m)')
    plt.ylabel('Drag force per unit length (N/m)')
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.tight_layout(rect=[0,0,1,0.78])
    plt.savefig('DragForcePerUnitLength.pdf')
    plt.close(fig)

def plotLiftDistrib():

    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(p1_caseData[i].spanLoc,p1_caseData[i].lfpul,label=p1_caseLabels[i])
    plt.plot(spanLoc,lfpul_liftingLine,label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.xlabel('Span location (m)')
    plt.ylabel('Lift force per unit length (N/m)')
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.tight_layout(rect=[0,0,1,0.78])
    plt.savefig('LiftForcePerUnitLength.pdf')
    plt.close(fig)

def plotTotForceCoeff():
    
    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(np.arange(p1_caseData[i].nTimesteps)*p1_caseData[i].dt, p1_caseData[i].TotLiftCoeff,label=p1_caseLabels[i])
    plt.axhline(CL_liftingLine,label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.xlabel('Time (s)')
    plt.ylabel('Lift coefficient')
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.tight_layout(rect=[0,0,1,0.78])
    plt.savefig('LiftCoeff.pdf')
    plt.close(fig)
    
    fig, ax = plt.subplots()
    ax.set_prop_cycle(colorcycle)
    for i in p1_cases:
        plt.plot(np.arange(p1_caseData[i].nTimesteps)*p1_caseData[i].dt, p1_caseData[i].TotDragCoeff,label=p1_caseLabels[i])
    plt.axhline(CD_liftingLine,label='Lifting line',color='k')
    ax.yaxis.set_major_locator(MaxNLocator(7))
    plt.xlabel('Time (s)')
    plt.ylabel('Drag coefficient')
    plt.legend(loc='lower center',ncol=2,bbox_to_anchor=(0.435, 1.01))
    plt.tight_layout(rect=[0,0,1,0.78])
    plt.savefig('DragCoeff.pdf')
    plt.close(fig)
    
if __name__=="__main__":
    
    plotAlpha()
    plotLiftDistrib()
    plotDragDistrib()
    plotTotForceCoeff()

    plotActuatorForce()    
    plotActuatorAoA()    
    
