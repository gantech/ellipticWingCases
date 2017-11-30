-----  AeroDyn Driver v1.00.x Input File  --------------------------------------
EllipticWing_Onshore_Aerodyn15.dat
-----  Input Configuration  ----------------------------------------------------
FALSE         Echo            -  Echo input parameters to "<rootname>.ech"?
"EllipticWing/EllipticWing_Onshore_Aerodyn15.dat"    AD_InputFile    -  Name of the primary AeroDyn input file
-----  Turbine Data  -----------------------------------------------------------
          2   NumBlades       - Number of blades (-)
        1.5   HubRad          - Hub radius (m)
      89.35   HubHt           - Hub height (m)
    -5.0191   Overhang        - Overhang (m)
        0     ShftTilt        - Shaft tilt (deg)
        0     Precone         - Blade precone (deg)
-----  I/O Settings  -----------------------------------------------------------
""            OutFileRoot     - Root name for any output files (use "" for .dvr rootname) (-)
True          TabDel          - When generating formatted output (OutForm=True), make output tab-delimited (fixed-width otherwise) (flag)
"ES15.6E3"    OutFmt          - Format used for text tabular output, excluding the time channel.  Resulting field should be 10 characters. (quoted string)
True          Beep            - Beep on exit (flag)
-----  Combined-Case Analysis  -------------------------------------------------
         1    NumCases        - Number of cases to run
WndSpeed       ShearExp       RotSpd        Pitch            Yaw           dT             Tmax
(m/s)            (-)          (rpm)         (deg)           (deg)          (s)            (s)
8.0000000E+00  0.0000000E+00  0.0      8.3000000E+01  -0.000000E+00       0.05            4     
                     
