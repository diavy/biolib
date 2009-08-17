import sys
sys.path += ['../libsequence']
#print sys.path
#import biolib.libsequence as libsequence
from biolib.libsequence import *

###################################################################
#####################Test1 Complement the Sequence#################
###################################################################

print "Test1: Complement the Sequence..."
name = raw_input("Please enter the name of sequence:")
seq = raw_input("Please enter the sequence itself:")
x = Fasta(name,seq)

count = stateCounter()
for s in seq:
    count(s)

if count.ndna == False:
    leng = x.length() - count.gap - count.n

    perA = (float)(count.a) / leng;
    perG = (float)(count.g) / leng;
    perC = (float)(count.c) / leng;
    perT = (float)(count.t) / leng;

    print "using Sequence::stateCounter:"
    print "A",perA
    print "G",perG
    print "C",perC
    print "T",perT

else:
    print "non-DNA character encountered. Skipping.\n"

print "\n\n\n"
    


######################################################################
#####################Test2 Translate the Sequence#####################
######################################################################
print "Test2: Translate the Sequence..."
alphabet = ('A','G','C','T');

codon = '';
for first in range(0,4):
    for second in range(0,4):
        for third in range(0,4):
            codon += alphabet[first]
            codon += alphabet[second]
            codon += alphabet[third]
            seq = Fasta('dna',codon)
            print codon,"\t",Translate(seq.begin_const(), seq.end_const())
            codon = ''

print "\n\n\n"


######################################################################
#####################Test3 Input/Output stream for various############
#########################data types in libsequence####################
######################################################################

print "Test3: Input/Output Stream for various data types:\n"
print """Note: if you want to see the print out result, you have to run the file
through bash shell, not Python shell!
      """
######################class Fasta###########################
#######input########
print "Fisrt read the fasta data from external file..."
fasta = Fasta()
infile = ifstream("../../../../test/data/fasta/example.fasta")
fasta.read(infile)
print
#######output#########
print "Next print out the sequence in FASTA format:\n"
fasta._print(cout)
print "\n\n"

###########################################################

#############class newick_stream_marginal_tree############
########output#########
outmarg = init_marginal(10)
n = newick_stream_marginal_tree(outmarg)
print "Print a marginal tree in Newick format:\n"
n._print(cout)
print "\n\n"
###########################################################

#########################class SimData#######################
#########input#############
print "First read the SimData data from external file..."
d = SimData()
infile = ifstream("../../../../test/data/simdata/simdata.txt")
d.read(infile)
print

########output#######
print "Next print out the SimData data: \n"
d._print(cout)
print "\n\n"
############################################################


##########################class PolySites###############################
############output####################
v = fastaVector(2)
v[0] = Fasta('s1','ATGCG')
v[1] = Fasta('s2','CG-TT')
p = PolySites(v)
print "Print out a PolySites format data:\n"
p._print(cout)
print "\n\n"

########################class SimpleSNP###############################
#########input############
print "First read the Simple SNP data from external file..."
snp = SimpleSNP()
fh = ifstream("../../../../test/data/simplesnp/simplesnp.txt")
snp.read(fh)

########output###########
print "Next print out the SimpleSNP data:\n"
snp._print(cout)
print





