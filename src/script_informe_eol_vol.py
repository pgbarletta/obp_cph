# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: eol_vol.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-13 12:13 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0=r"""
using DataFrames, FileIO, DelimitedFiles
using Plots, Optim, LsqFit, JUMD
using Statistics, NamedArrays
""".strip()

cell_1=r"""
# Get ready
dir_eol_vol = "/home/pbarletta/labo/20/cph_obp/run/eol/cavidad"

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
    global vol_eol_idx = convert(Array{Float64, 1}, readdlm(joinpath(dir_eol_vol, string(idx[i]),
            string("vol_trj_eol_", idx[i])))[:, 3])
    global vol_eol_phs = convert(Array{Float64, 1}, readdlm(joinpath(dir_eol_vol, string(phs[i], "ph"),
            string("vol_trj_eol_", phs[i])))[:, 3])

    sym_vol_trj_eol_idx = Symbol("vol_trj_eol_", idx[i])
    sym_vol_trj_eol_phs = Symbol("vol_trj_eol_", phs[i])
    eval(:($sym_vol_trj_eol_idx = vol_eol_idx))
    eval(:($sym_vol_trj_eol_phs = vol_eol_phs))
end
""".strip()

cell_3=r"""
## vol por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3),
]

for ph in range(30, 80, 5):
    celda_ph=(r"""plot(collect(1:nstlim) ./ 100, vol_trj_eol_""" + str(ph) + r""", 
        title = string("Volume - pH = ", """ + str(ph) + r"""), size = (750, 400),
        ylims = (1, 2000), label = false,
        linecolor = Colors.colorant"Brown",
        yaxis = "Volume [A3]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))

    celda_ph_his=(r"""
        max_vol = 2000
        st = 20
        bin_vol = collect(0:st:max_vol)
        wgh_vol = fill(1.0, length(vol_trj_eol_""" + str(ph) + r"""))
        
        # Histograma ponderado
        Wbins_vol, Whis_vol = JUMD.weightedHist(vol_trj_eol_""" + str(ph) + r""", bin_vol, wgh_vol, true, false);
        
        bar(Wbins_vol, Whis_vol,
            xlims = (0, 800), ylims = (0, .2),
            xticks = 100:100:700,
            linecolor = false, fillcolor = Colors.colorant"Brown",
            grid = false, legend = false,
            guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
            legendfont = font(12, "Arial"),
            title = string("Volume histogram - pH = ", """ + str(ph) + r"""), yaxis = "Relative probability", xaxis = "Volume")
        """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_his))

celda_tabla_ph=r"""vals = vcat("""
for ph in range(30, 80, 5):
    if ph == 75:
        celda_tabla_ph= celda_tabla_ph + (r"""
        [ mean(vol_trj_eol_""" + str(ph) + r""") std(vol_trj_eol_""" + str(ph) + r""") std(vol_trj_eol_""" + str(ph) + r""") / mean(vol_trj_eol_""" + str(ph) + r""") ])""").strip() + "\n" + "\n"
        break

    celda_tabla_ph= celda_tabla_ph + (r"""
    [ mean(vol_trj_eol_""" + str(ph) + r""") std(vol_trj_eol_""" + str(ph) + r""") std(vol_trj_eol_""" + str(ph) + r""") / mean(vol_trj_eol_""" + str(ph) + r""") ],""").strip() + "\n"

celda_tabla_ph= celda_tabla_ph + r"""NamedArray(vals, (string.(phs), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_ph))

celda_titulo=r"""
## vol por idx
""".strip()
nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 11):
    celda_idx=(r"""
    plot(collect(1:nstlim) ./ 100, vol_trj_eol_""" + str(idx) + r""", 
        title = string("Volume - idx = ", """ + str(idx) + r"""), size = (750, 400),
        ylims = (1, 2000), label = false,
        linecolor = Colors.colorant"CornflowerBlue",
        yaxis = "Volume [A3]", xaxis = "Time [ns]")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx))
 
    celda_idx_his=(r"""
    max_vol = 2000
    st = 20
    bin_vol = collect(0:st:max_vol)
    wgh_vol = fill(1.0, length(vol_trj_eol_""" + str(idx) + r"""))
    
    # Histograma ponderado
    Wbins_vol, Whis_vol = JUMD.weightedHist(vol_trj_eol_""" + str(idx) + r""", bin_vol, wgh_vol, true, false);
    
    bar(Wbins_vol, Whis_vol,
        xlims = (0, 800), ylims = (0, .2),
        xticks = 100:100:700,
        linecolor = false, fillcolor = Colors.colorant"CornflowerBlue",
        grid = false, legend = false,
        guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
        legendfont = font(12, "Arial"),
        title = string("Volume histogram - idx = ", """ + str(idx) + r"""), yaxis = "Relative probability", xaxis = "Volume")
    """).strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx_his))

    celda_tabla_idx=(r"""NamedArray([ mean(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") / mean(vol_trj_eol_""" + str(idx) + r""") ],
    (["Volume"], ["μ" ; "std" ; "μ/std"]))""").strip()
    nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_idx))


celda_tabla_idx=r"""vals = vcat("""
for idx in range(1, 11):
    if idx == 10:
        celda_tabla_idx= celda_tabla_idx + (r"""
        [ mean(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") / mean(vol_trj_eol_""" + str(idx) + r""") ])""").strip() + "\n" + "\n"
        break

    celda_tabla_idx= celda_tabla_idx + (r"""
    [ mean(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") std(vol_trj_eol_""" + str(idx) + r""") / mean(vol_trj_eol_""" + str(idx) + r""") ],""").strip() + "\n"

celda_tabla_idx= celda_tabla_idx + r"""NamedArray(vals, (string.(idx), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_idx))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_eol_vol.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_eol_vol.ipynb successfully generated.")