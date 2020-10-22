# -*- coding: utf-8 -*-
# `nb_templater` generated Python script
# Generated from .ipynb template: apo_hbo.ipynb
# www.github.com/ismailuddin/jupyter-nb-templater/
# Generated on: 2020-10-20 18:36 

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
dir_apo_hbo = "/home/pbarletta/labo/20/cph_obp/run/apo/hbond"

aa = 119
nstlim = 19500
phs = collect(30:5:75)
idx = collect(1:10)
pdt_steps = collect(0:1:7)
titratable_cnt = 36
titratable_resis = [4, 5, 7, 11, 13, 18, 20, 24, 27, 30, 33, 37, 39,
    40, 41, 42, 48, 52, 58, 59, 64, 69, 73, 77, 78, 82, 87, 93, 94,
    97, 99, 102, 109, 111, 114, 117];
titratable_resnames = ["GL4", "GL4", "LYS", "HIP", "GL4", "LYS", "GL4", "AS4", "LYS",
    "AS4", "GL4", "AS4", "GL4", "AS4", "LYS", "LYS", "GL4", "LYS",
    "AS4", "LYS", "LYS", "LYS", "GL4", "AS4", "GL4", "LYS", "AS4",
    "GL4", "GL4", "HIP", "LYS", "LYS", "LYS", "LYS", "LYS", "AS4"]

idx_of_titratable = fill(0, aa)
[ idx_of_titratable[titratable_resis[i]] = i for i in 1:titratable_cnt ];

titratable_residues = [ string(titratable_resnames[i], "_", titratable_resis[i]) 
    for i in 1:titratable_cnt ];
""".strip()

cell_2=r"""
for i in 1:10
    global nhb_apo_idx = convert(Array{Float64, 1}, readdlm(joinpath(dir_apo_hbo, string(idx[i]),
            string("nhb_apo_", idx[i])))[2:end, 2])
    global nhb_apo_phs = convert(Array{Float64, 1}, readdlm(joinpath(dir_apo_hbo, string(phs[i], "ph"),
            string("nhb_apo_", phs[i])))[2:end, 2])

    sym_nhb_apo_idx = Symbol("nhb_apo_", idx[i])
    sym_nhb_apo_phs = Symbol("nhb_apo_", phs[i])
    eval(:($sym_nhb_apo_idx = nhb_apo_idx))
    eval(:($sym_nhb_apo_phs = nhb_apo_phs))
end
""".strip()

cell_3=r"""
## hbonds count por pH
""".strip()

nb['cells'] = [
    nbf.v4.new_code_cell(cell_0),
    nbf.v4.new_code_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_markdown_cell(cell_3)
]

for ph in range(30, 80, 5):
    celda_ph = (r"""min_nhb = 20
    max_nhb = 90
    plot(collect(1:nstlim) ./ 100, nhb_apo_""" + str(ph) + r""",
        title = string("Total # of Hbonds - pH = ",""" + str(ph) + r"""), size = (750, 400),
        ylims = (min_nhb, max_nhb), label = false,
        linecolor = Colors.colorant"Brown",
        yaxis = "# of Hbonds", xaxis = "Time [ns]")
    """).strip()

    celda_ph_his=(r"""
    st = 2
    bin_nhb = collect(min_nhb:st:max_nhb)
    wgh_nhb = fill(1.0, length(nhb_apo_""" + str(ph) + r"""))
    
    # Histograma ponderado
    Wbins_nhb, Whis_nhb = JUMD.weightedHist(nhb_apo_""" + str(ph) + r""", bin_nhb, wgh_nhb, true, false);
    
    bar(Wbins_nhb, Whis_nhb,
        xlims = (min_nhb, max_nhb), ylims = (0, .2),
        xticks = min_nhb+st:10:max_nhb+st,
        linecolor = false, fillcolor = Colors.colorant"Brown",
        grid = false, legend = false,
        guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
        legendfont = font(12, "Arial"),
        title = string("Total # of Hbonds histogram - pH = ",""" + str(ph) + r"""),
        yaxis = "Relative probability", xaxis = "# of Hbonds")
    """).strip()
    
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph))
    nb['cells'].append(nbf.v4.new_code_cell(celda_ph_his))


celda_tabla_ph=r"""vals = vcat("""
for ph in range(30, 80, 5):
    if ph == 75:
        celda_tabla_ph = celda_tabla_ph + (r"""
        [ mean(nhb_apo_""" + str(ph) + r""") std(nhb_apo_""" + str(ph) + r""") std(nhb_apo_""" + str(ph) + r""") / mean(nhb_apo_""" + str(ph) + r""") ])""").strip() + "\n" + "\n"
        break

    celda_tabla_ph = celda_tabla_ph + (r"""
    [ mean(nhb_apo_""" + str(ph) + r""") std(nhb_apo_""" + str(ph) + r""") std(nhb_apo_""" + str(ph) + r""") / mean(nhb_apo_""" + str(ph) + r""") ],""").strip() + "\n"
    
    
celda_tabla_ph= celda_tabla_ph + r"""NamedArray(vals, (string.(phs), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_ph))

celda_titulo=r"""
## hbonds count por idx
""".strip()
nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))

for idx in range(1, 11):
    celda_idx=(r"""
    plot(collect(1:nstlim) ./ 100, nhb_apo_""" + str(idx) + r""",
        title = string("nhbume - idx = ", """ + str(idx) + r"""), size = (750, 400),
        ylims = (min_nhb, max_nhb), label = false,
        linecolor = Colors.colorant"CornflowerBlue",
        yaxis = "nhbume [A3]", xaxis = "Time [ns]")
    """).strip()
    
    celda_idx=(r"""
    st = 2
    bin_nhb = collect(min_nhb:st:max_nhb)
    wgh_nhb = fill(1.0, length(nhb_apo_""" + str(idx) + r"""))
    
    # Histograma ponderado
    Wbins_nhb, Whis_nhb = JUMD.weightedHist(nhb_apo_""" + str(idx) + r""", bin_nhb, wgh_nhb, true, false);
    
    bar(Wbins_nhb, Whis_nhb,
        xlims = (min_nhb, max_nhb), ylims = (0, .2),
        xticks = min_nhb+st:10:max_nhb+st,
        linecolor = false, fillcolor = Colors.colorant"CornflowerBlue",
        grid = false, legend = false,
        guidefont = font(18, "Arial"), tickfont = font(12, "Arial"),
        legendfont = font(12, "Arial"),
        title = string("H bonds count histogram - pH = ", """ + str(idx) + r"""),
        yaxis = "Relative probability", xaxis = "# of Hbonds")
    """).strip()

    nb['cells'].append(nbf.v4.new_code_cell(celda_idx))
    nb['cells'].append(nbf.v4.new_code_cell(celda_idx))


celda_tabla_idx=r"""vals = vcat("""
for idx in range(1, 11):
    if idx == 10:
        celda_tabla_idx = celda_tabla_idx + (r"""
        [ mean(nhb_apo_""" + str(idx) + r""") std(nhb_apo_""" + str(idx) + r""") std(nhb_apo_""" + str(idx) + r""") / mean(nhb_apo_""" + str(idx) + r""") ])""").strip() + "\n" + "\n"
        break

    celda_tabla_idx = celda_tabla_idx + (r"""
    [ mean(nhb_apo_""" + str(idx) + r""") std(nhb_apo_""" + str(idx) + r""") std(nhb_apo_""" + str(idx) + r""") / mean(nhb_apo_""" + str(idx) + r""") ],""").strip() + "\n"
    
    
celda_tabla_idx= celda_tabla_idx + r"""NamedArray(vals, (string.(idx), ["μ" ; "std" ; "μ/std"]))"""
nb['cells'].append(nbf.v4.new_code_cell(celda_tabla_idx))

celda_tituol=r"""
## Conteo de puentesH de residuos titulables
""".strip()
nb['cells'].append(nbf.v4.new_markdown_cell(celda_titulo))


cell_12=r"""
nhb_cnt_apo_acc_phs = Array{Int64, 2}(undef, aa, 0)
nhb_cnt_apo_don_phs = Array{Int64, 2}(undef, aa, 0)

for ph in phs
    nhb_ser_apo_acc_ph = fill(0, (aa, nstlim))
    nhb_ser_apo_don_ph = fill(0, (aa, nstlim))
    
    temporal_acc = readdlm(joinpath(dir_apo_hbo, string(ph, "ph"),
        string("series_nhb_apo_gl4_as4_lys_acc_", ph)), header = true)
    
    temporal_don = readdlm(joinpath(dir_apo_hbo, string(ph, "ph"),
        string("series_nhb_apo_gl4_as4_lys_don_", ph)), header = true)
    
    res_hbo_apo_acc_phs = convert(Array{Bool, 2}, temporal_acc[1][:, 2:end])
    acceptor_donor_acc = convert(Array{String, 1}, temporal_acc[2][2:end])
    
    res_hbo_apo_don_phs = convert(Array{Bool, 2}, temporal_don[1][:, 2:end])
    acceptor_donor_don = convert(Array{String, 1}, temporal_don[2][2:end])
    

    for i = 1:nstlim  
        mascara_acc = findall(res_hbo_apo_acc_phs[i, :])
        mascara_don = findall(res_hbo_apo_don_phs[i, :])
        
        for j in mascara_acc
            acceptor, donor = split(acceptor_donor_acc[j], "-")
            don = parse(Int64, split(split(donor, "_")[2], "@")[1])
            acc = parse(Int64, split(split(acceptor, "_")[2], "@")[1])
            nhb_ser_apo_acc_ph[don, i] += 1
            nhb_ser_apo_acc_ph[acc, i] += 1
        end
        
        for j in mascara_don
            acceptor, donor = split(acceptor_donor_don[j], "-")
            acc = parse(Int64, split(split(acceptor, "_")[2], "@")[1])
            don = parse(Int64, split(split(donor, "_")[2], "@")[1])
            nhb_ser_apo_don_ph[don, i] += 1
            nhb_ser_apo_don_ph[acc, i] += 1
        end
    end

    nhb_cnt_apo_acc_ph = mapslices(x -> sum(x), nhb_ser_apo_acc_ph, dims = 2)[:, 1]
    global nhb_cnt_apo_acc_phs = hcat(nhb_cnt_apo_acc_phs, nhb_cnt_apo_acc_ph)
    
    nhb_cnt_apo_don_ph = mapslices(x -> sum(x), nhb_ser_apo_don_ph, dims = 2)[:, 1]
    global nhb_cnt_apo_don_phs = hcat(nhb_cnt_apo_don_phs, nhb_cnt_apo_don_ph)
    
end
""".strip()

cell_13=r"""
nhb_cnt_apo_phs = nhb_cnt_apo_acc_phs .+ nhb_cnt_apo_don_phs;
""".strip()

cell_14=r"""
heatmap(titratable_residues[1:12], (phs ./ 10), nhb_cnt_apo_phs[titratable_resis[1:12], :],
    xrotation = 60, color = :bilbao)
""".strip()

cell_15=r"""
heatmap(titratable_residues[13:24], (phs ./ 10), nhb_cnt_apo_phs[titratable_resis[13:24], :],
    xrotation = 60, color = :bilbao)
""".strip()

cell_16=r"""
heatmap(titratable_residues[25:end], (phs ./ 10), nhb_cnt_apo_phs[titratable_resis[25:end], :],
    xrotation = 60, color = :bilbao)
""".strip()

nb['cells'].append(nbf.v4.new_code_cell(cell_12))
nb['cells'].append(nbf.v4.new_code_cell(cell_13))
nb['cells'].append(nbf.v4.new_code_cell(cell_14))
nb['cells'].append(nbf.v4.new_code_cell(cell_15))
nb['cells'].append(nbf.v4.new_code_cell(cell_16))


nb['metadata'] = {'kernelspec': {'display_name': 'Julia 1.5.0', 'language': 'julia', 'name': 'julia-1.5'}}


nbf.write(nb, r'/home/pbarletta/labo/20/cph_obp/src/informe_apo_hbo.ipynb')
print(r"Jupyter notebook /home/pbarletta/labo/20/cph_obp/src/informe_apo_hbo.ipynb successfully generated.")
