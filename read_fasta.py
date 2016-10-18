# Reads a fasta file and prints the sequence to standard out.

import sys

def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "<sequence.fa>"
    exit(1)

# end of the analysis
<<<<<<< HEAD
print read_fasta(sys.argv[1])
=======
print read_fasta(sys.argv[1])
>>>>>>> add-docs
