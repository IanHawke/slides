import glob
import shutil
import os

for x in glob.glob('img*/*'):
    if not x.endswith('_notitle.png'):
        os.remove(x)
