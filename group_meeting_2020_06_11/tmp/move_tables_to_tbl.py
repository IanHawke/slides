# Small script to rename tables to somethign more overleaf friendly
import os
import glob
import sys

with open(sys.argv[1]) as f:
    tex = f.read()

for f in glob.glob("tables/*"):
    newname = f.replace(".tex", ".tbl")
    os.system("git mv {} {}".format(f, newname))
    tex = tex.replace(f, newname)

with open(sys.argv[1], 'w') as f:
    f.write(tex)
