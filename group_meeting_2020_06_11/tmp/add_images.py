import sys
import os
import shutil
import glob

norms = ['wasserstein_speedup_real', 'wasserstein_speedup_raw', 'prediction_l2']
added = 0
texfile = ""
for norm in norms:
    comparisons = glob.glob('../learning_airfoils/notebooks/img/*comparison*{norm}*_128_ordinary_best*'.format(norm=norm))
    added += len(comparisons)

    base = """
\\begin{{figure}}
    \\includegraphics[width=\\textwidth]{{{img}}}
    \\caption{{{img_safe}}}
\\end{{figure}}
\\clearpage
"""
    for comparison in comparisons:
        destination = comparison.replace('../learning_airfoils/notebooks/', '')
        shutil.copyfile(comparison, destination)
        os.system('git add {}'.format(destination))
        texfile += base.format(img=destination,
                               img_safe = destination.replace("_", "\\_"))

with open('added_plots.tex', 'w') as f:
    f.write(texfile)
print(added)
