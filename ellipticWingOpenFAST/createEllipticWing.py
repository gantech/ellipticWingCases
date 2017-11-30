import numpy as np
small = 1e-6
def createFAST_EllipticWingBlade(span, nNodes):

    dx = span/(nNodes-1.0)
    x = np.arange(0,span+small, dx) - span*0.5
    c = np.sqrt(1.0 - (2.0*x/span)**2)
    c[0] = small
    c[-1] = small

    with open('EllipticWing_Aerodyn_Blade.dat','w') as f:

        f.write('------- AERODYN v15.00.* BLADE DEFINITION INPUT FILE -------------------------------------\n')
        f.write('Elliptic wing\n')
        f.write('======  Blade Properties =================================================================\n')
        f.write('{}   NumBlNds           - Number of blade nodes used in the analysis (-)\n'.format(nNodes))
        f.write('BlSpn        BlCrvAC        BlSwpAC        BlCrvAng       BlTwist        BlChord          BlAFID\n')
        f.write('(m)           (m)            (m)            (deg)         (deg)           (m)              (-)\n')

        for i in range(nNodes):
            print x[i]+span*0.5
            f.write('{}  0.0000000E+00  0.0000000E+00 0.0000000E+00  0.0000000E+00  {}        1\n'.format(x[i]+span*0.5, c[i] ))

    
if __name__ == "__main__":

    createFAST_EllipticWingBlade(10, 18)
    
