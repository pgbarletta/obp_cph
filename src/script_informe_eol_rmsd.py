# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_rmsd.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-12 20:00 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit
""".strip()

cell_1=r"""
# Get ready
home = "/home/pbarletta/labo/20/cph_obp/"
dir_eol_pdt = string(home, "run/eol/pdt/")
dir_eol_all_pdt = string(home, "run/eol/all_pdt/")

nstlim = 19500
phs = collect(30:5:75)
idx = collect(1:10)
pdt_steps = collect(0:1:7)
titrable_cnt = 36
titrable_resis = [4, 5, 7, 11, 13, 18, 20, 24, 27, 30, 33, 37, 39,
    40, 41, 42, 48, 52, 58, 59, 64, 69, 73, 77, 78, 82, 87, 93, 94,
    97, 99, 102, 109, 111, 114, 117];
titrable_resnames = ["GL4", "GL4", "LYS", "HIP", "GL4", "LYS", "GL4", "AS4", "LYS",
    "AS4", "GL4", "AS4", "GL4", "AS4", "LYS", "LYS", "GL4", "LYS",
    "AS4", "LYS", "LYS", "LYS", "GL4", "AS4", "GL4", "LYS", "AS4",
    "GL4", "GL4", "HIP", "LYS", "LYS", "LYS", "LYS", "LYS", "AS4"];
""".strip()

cell_2=r"""
for i in 1:10
    global rmsd_eol_idx = readdlm(joinpath(dir_eol_pdt, string(phs[i], "ph"),
            string("rmsd_eol_", idx[i])))[2:end, 2]
    global rmsd_eol_ph = readdlm(joinpath(dir_eol_all_pdt, string(phs[i], "ph"),
            string("rmsd_eol_", phs[i])))[2:end, 2]

    sym_rmsd_eol_idx = Symbol("rmsd_eol_", idx[i])
    sym_rmsd_eol_ph = Symbol("rmsd_eol_", phs[i])
    eval(:($sym_rmsd_eol_idx = rmsd_eol_idx))
    eval(:($sym_rmsd_eol_ph = rmsd_eol_ph))
end
""".strip()

cell_3=r"""
## RMSD por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3)
]

for ph in range(30, 80, 5):
    celda_ph = (r"""plot(collect(1:nstlim) ./ 100, """ + "rmsd_eol_" + str(ph) + r""", 
        title = string("RMSD - pH = ", """ + str(ph) + r"""), size = (750, 400),
        yaxis = "RMSD [A]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))

celda_titulo=r"""
## RMSD por idx
""".strip()

nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 11):
    celda_idx = (r"""plot(collect(1:nstlim) ./ 100, """ + "rmsd_eol_" + str(idx) + r""", 
        title = string("RMSD - idx = ", """ + str(idx) + r"""), size = (750, 400),
        yaxis = "RMSD [A]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx))



nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_eol_rmsd.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_eol_rmsd.ipynb successfully generated.")
