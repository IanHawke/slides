import sys
import os
import shutil
import glob
import re
import json
import glob
def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))


if len(sys.argv) != 2:
    print("Usage:\n\tpython {} <path to experimetns folder (should contain notebooks/img)>".format(sys.argv[0]))
    sys.exit(1)

basepath = sys.argv[1]


best_networks_filename = os.path.join(basepath, 'data/best_networks.json')

with open(best_networks_filename) as best_networks_file:
    best_networks = json.load(best_networks_file)



table_names = {
    'Prediction errors (relative) with variance' : 'prediction_errors_with_std',
    'Prediction errors (relative) with variance (keeping training samples)' : 'prediction_errors_with_std_ts',
    'Speedups using MC evaluation points, against MC sample data (trained on QMC data)' : 'mc_speedups_mc',
    'Speedups using QMC evaluation points, against MC sample data (trained on QMC data)' : 'mc_speedups_qmc_from_data',
    'Speedups (error mc qmc)/(error ml qmc) using MC evaluation points, against MC sample data (trained on QMC data)' : 'mc_speedups_vs_qmc_mc',
    'Speedups (error mc qmc)/(error ml qmc) using QMC evaluation points, against MC sample data (trained on QMC data)' : 'mc_speedups_vs_qmc_qmc_from_data',
    'Errors using MC evaluation points, against MC sample data (trained on QMC data)' : 'mc_errors_mc',
    'Errors using QMC evaluation points, against MC sample data (trained on QMC data)' : 'mc_errors_qmc_from_data',
    
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
    

only_once_per_func = []

texfile = ""

added = 0

for table_name in table_names.keys():
    texfile += '\\subsection{{{}}}\n'.format(table_name)
    for network_name in best_networks.keys():
        for functional_name in functionals.keys():
            
            if network_name.lower() not in functional_name.lower() and network_name != 'effective':
                continue
            texfile += '\\subsubsection{{{}}}\n'.format(functional_name)
            files = insensitive_glob(os.path.join(basepath, "notebooks/tables/{}_*{}.tex".format(functionals[functional_name], table_names[table_name])))
        
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

                if abs(float(regularization_size) - best_networks[network_name]['regularization'][regularization_type]) >= min(float(regularization_size), best_networks[network_name]['regularization'][regularization_type])*4:
                    continue

                destination = f.replace('{basepath}/notebooks/'.format(basepath=basepath), '')
                shutil.copyfile(f, destination)
                typename = 'best performing'
                if network_name == 'effective':
                    typename = 'effective'
                base = """
\\begin{{figure}}
    \\input{{{img}}}
    \\caption{{{title} ({img_safe})}}
\\end{{figure}}
\\clearpage
"""
                texfile += base.format(img=destination, img_safe=destination.replace('_',"\\_"),
                                   title="({} network) {} for {}".format(typename, table_name, functional_name))
            
                added += 1
                os.system('git add {}'.format(destination))

with open('added_individual_tables.tex', 'w') as f:
    f.write(texfile)
print(added)
