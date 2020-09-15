import glob
import sys
import os.path
import shutil
with open(sys.argv[1]) as f:
    content = f.read()
    
for x in glob.glob('img/*'):
    if os.path.basename(x).replace('.png', '') not in content:
        shutil.move(x, os.path.join('../deleted/', os.path.basename(x)))
