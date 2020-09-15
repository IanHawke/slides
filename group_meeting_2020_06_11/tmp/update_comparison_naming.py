# updates the naming from old comparison to new
import sys
import os
import shutil
import glob

if len(sys.argv) != 3:
    print("Usage\n\tpython {} sourcefolder texfile".format(sys.argv[0]))
    exit(1)
updates = [["wasserstein", "wasstrain"],
           ["rayprediction", "val"]]

tex = sys.argv[2]
with open(tex) as f:
    tex_content = f.read()
    
source = sys.argv[1]
for img in glob.glob('img/*comparison*.png'):
    basename = os.path.basename(img).replace('.png', "").replace("_notitle", "")

    if basename in tex_content:
        newname = basename
        for update in updates:
            newname = newname.replace(update[0], update[1])

        endings = [".png", "_notitle.png"]
        for ending in endings:
            filename = newname + ending
            sourcename = os.path.join(source, filename)
            if os.path.exists(sourcename):
                shutil.copyfile(sourcename, os.path.join('img', filename))
                os.system('git add {}'.format(os.path.join('img', filename)))
        tex_content = tex_content.replace(basename, newname)
with open(tex, 'w') as f:
    f.write(tex_content)
