import sys
import os
import shutil
import glob
import re
import json


if len(sys.argv) != 2:
    print("Usage:\n\tpython {} <path to experimetns folder (should contain notebooks/img)>".format(sys.argv[0]))
    sys.exit(1)

basepath = sys.argv[1]


best_networks_filename = os.path.join(basepath, 'data/best_networks.json')

with open(best_networks_filename) as best_networks_file:
    best_networks = json.load(best_networks_file)



plot_names = {'Generalization plot (ML)' : 'scatter_ml',
              'Generalization plot (LSQ)' : 'scatter_lsq',
              'Histogram comparison QMC versus ML' : 'hist_qmc_ml',
              'Histogram comparison QMC versus LSQ' : 'hist_qmc_lsq',
              'Histogram comparison QMC versus QMC with fewer samples' : 'hist_qmc_qmc',
              'Histogram comparison QMC versus ML' : 'hist_qmc_ml',
              'Training and validation error' : 'training_validation_loss',
              'Error evolution of Wasserstein distance' : 'error_evolution_wasserstein'
}

functionals = {
    'Sod Shock tube Q1' : 'sodshocktubeqmcq1',
    'Sod Shock tube Q2' : 'sodshocktubeqmcq2',
    'Sod Shock tube Q3' : 'sodshocktubeqmcq3',
    '$\\sum_{k=1}^6\\sin(4\pi x_k)$' : 'sinesine',
    '$\\sum_{k=1}^6\\sin(4\pi x_k)/k$' : 'sinesined',
    '$\\sum_{k=1}^6\\sin(4\pi x_k)/k^3$' : 'sinesined3',
    'Airfoils Lift' : 'airfoilslift',
    'Airfoils Drag' : 'airfoilsdrag'}
    

only_once_per_func = ['hist_qmc_lsq', 'scatter_lsq', 'hist_qmc_qmc']

texfile = ""
added_plots = {}
for func in functionals.keys():
    added_plots[func] = {}

added = 0

for plot_name in plot_names.keys():
    texfile += '\\subsection{{{}}}\n'.format(plot_name)
    for network_name in best_networks.keys():
        for functional_name in functionals.keys():
            if network_name.lower() not in functional_name.lower() and network_name != 'effective':
                continue
            if plot_name in only_once_per_func and plot_name in added_plots[func].keys():
                continue

            texfile += '\\subsubsection{{{}}}\n'.format(functional_name)
            added_plots[func][plot_name] = True
        
            files = glob.glob(os.path.join(basepath, "notebooks/img/{}_*{}.png".format(functionals[functional_name], plot_names[plot_name])))
        
            for f in files:


                regularization_match = re.search(r'_(l[1-2])(\d+e\d+)', os.path.basename(f))
                regularization_type = regularization_match.group(1)
                regularization_size = regularization_match.group(2)

                regularization_size = regularization_size.replace('e', 'e-')
                regularization_size = float("{}.{}".format(regularization_size[0], regularization_size[1:]))


                selection = best_networks[network_name]['selection']
                loss = best_networks[network_name]['loss']
                
                if selection.lower() not in f:
                    continue
                if loss.lower() not in f:
                    continue

                if abs(regularization_size - best_networks[network_name]['regularization'][regularization_type]) >= min(float(regularization_size), best_networks[network_name]['regularization'][regularization_type])*4:
                    continue

                destination = f.replace('{basepath}/notebooks/'.format(basepath=basepath), '')
                shutil.copyfile(f, destination)
                shutil.copyfile(f.replace('.png', '_notitle.png'), destination.replace('.png', '_notitle.png'))
                network_type = 'best performing'
                if network_name == 'effective':
                    network_type = 'effective'
                base = """
\\begin{{figure}}
    \\includegraphics[width=\\textwidth]{{{img}}}
    \\caption{{{title} ({img_safe})}}
\\end{{figure}}
\\clearpage
"""
                texfile += base.format(img=destination, img_safe=destination.replace('_',"\\_"),
                                   title="({} network) {} for {}".format(network_type, plot_name, functional_name))
            
                added += 1
                os.system('git add {}'.format(destination))
                os.system('git add {}'.format(destination.replace('.png', '_notitle.png')))

with open('added_individual_plots.tex', 'w') as f:
    f.write(texfile)
print(added)
