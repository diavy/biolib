import sys
sys.path += ['../libsequence']
#print sys.path
#import biolib.libsequence as libsequence
from biolib.libsequence import *


############class Fasta##############################
#######input########
fas = Fasta()
infile = ifstream("../../../../test/data/fasta/example.fasta")
fas.read(infile)
print fas.GetName()
print fas.GetSeq()
print

