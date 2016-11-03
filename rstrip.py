name=raw_input('file path')
file = open("newfile.tsv", "w")

f = open(name, "r")
for line in f:
    line = line.rstrip()
    file.write(line+"\n")
f.close
file.close

import os

os.rename(name, name+"_old")
os.rename("newfile.tsv", name)

#/Users/gricelab/documents/Club_Grice/mapping_files/run_maps/MiSeq_32.tsv