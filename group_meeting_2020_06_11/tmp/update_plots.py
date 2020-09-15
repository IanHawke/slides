import os
import glob
import shutil
import sys

source = sys.argv[1]
texname = sys.argv[2]

with open(texname) as f:
    texcontent = f.read()

images = glob.glob('img/*.png')

added = 0
added_notitle = 0
for img in images:
    basename = os.path.basename(img).replace('.png', '').replace('_notitle', '')

    if basename in texcontent:
        print(basename)
        pngname = os.path.join(source, basename + '.png')
        print(pngname)
        pngnotitlename = os.path.join(source, basename + '_notitle.png')
        if os.path.exists(pngname):
            shutil.copyfile(pngname, pngname.replace(source, './img/'))
            added += 1
            os.system('git add {}'.format(pngname.replace(source, './img/')))
        if os.path.exists(pngnotitlename):
            shutil.copyfile(pngnotitlename, pngnotitlename.replace(source, './img/'))
            os.system('git add {}'.format(pngnotitlename.replace(source, './img/')))
            added_notitle +=1 
print(added)
print(added_notitle)
