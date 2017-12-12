(TeX-add-style-hook
 "ellipticWing"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("subfig" "caption=false")))
   (TeX-run-style-hooks
    "latex2e"
    "jfm"
    "jfm10"
    "graphicx"
    "epstopdf"
    "epsfig"
    "subfig")
   (LaTeX-add-labels
    "sec:intro"
    "sec:ll_soln"
    "fig:domain_illustration"
    "eqn:sim_parameters"
    "tab:gr"
    "subfig:CL"
    "subfig:CD"
    "fig:CL_CD"
    "subfig:lpul"
    "fig:lpul_dpul"
    "fig:aoa"
    "fig:act_l_act_d")
   (LaTeX-add-environments
    "lemma"
    "corollary")
   (LaTeX-add-bibliographies
    "references"))
 :latex)

