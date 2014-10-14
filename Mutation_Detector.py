# This file is part of Mutation-Detector.
# Copyright (C) 2014 Christopher Kyle Horton <chorton@ltu.edu>

# Mutation-Detector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Mutation-Detector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Mutation-Detector. If not, see <http://www.gnu.org/licenses/>.


# MCS 5603 Intro to Bioinformatics, Fall 2014
# Christopher Kyle Horton (000516274), chorton@ltu.edu
# Last modified: 10/14/2014

import argparse

import central_dogma as cd
import sequence_comparison

version = "v0.0.0"
desc = "Mutation Detector " + version
desc += "\nA utility for finding mutations between FASTA sequences."
infile_help="""
Takes three strings indicating coding or template, 3' or 5', and filename.
"""

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=desc
            )
parser.add_argument("infile1", help=infile_help, nargs=3)
parser.add_argument("infile2", help=infile_help, nargs=3)
parser.add_argument("-o", "--outfile", help="Filename for the output file",
                    type=str)
comparison_group = parser.add_mutually_exclusive_group()
comparison_group.add_argument("-d", "--DNA", help="Compare as 5' coding DNA.", action="store_true")
comparison_group.add_argument("-r", "--mRNA", help="Compare as mRNA.", action="store_true")
comparison_group.add_argument("-p", "--protein", help="Compare as proteins.", action="store_true")
comparison_group.add_argument("-a", "--all", help="Compare as DNA, mRNA, and proteins.", action="store_true")
args = parser.parse_args()
print args

outfile = ""
if args.outfile:
    outfile = args.outfile

# Read in sequences from FASTA files
# Ignore first line since that's just header info, not part of the sequence
sequence1 = sequence2 = ""
with open(args.infile1[2], 'r') as infile1_reading:
    lines1 = infile1_reading.readlines()[1:]
with open(args.infile2[2], 'r') as infile2_reading:
    lines2 = infile2_reading.readlines()[1:]
for line in lines1:
    sequence1 += line.upper().strip()
for line in lines2:
    sequence2 += line.upper().strip()

# Debug
print "Sequence 1:"
print sequence1
print "Sequence 2:"
print sequence2

if args.infile1[0] in ["t", "template"]:
    print "Sequence 1 is ", args.infile1[0], "; complementing..."
    sequence1 = cd.complement_DNA(sequence1)
if args.infile2[0] in ["t", "template"]:
    print "Sequence 2 is ", args.infile1[0], "; complementing..."
    sequence2 = cd.complement_DNA(sequence2)

if args.infile1[1] in ["3'", "3"]:
    print "Sequence 1 is 3'; reversing..."
    sequence1 = cd.reverse_sequence(sequence1)
if args.infile2[1] in ["3'", "3"]:
    print "Sequence 2 is 3'; reversing..."
    sequence2 = cd.reverse_sequence(sequence2)

if args.DNA:
    sequence_comparison.compare_sequences(sequence1, sequence2, args.outfile)
    exit(0)

# Debug
print "Sequence 1:"
print sequence1
print "Sequence 2:"
print sequence2

mRNA1 = cd.transcribe_coding_sequence(sequence1)
mRNA2 = cd.transcribe_coding_sequence(sequence2)

if args.mRNA:
    sequence_comparison.compare_sequences(mRNA1, mRNA2, args.outfile)
    exit(0)

# Debug
print "mRNA 1:"
print mRNA1
print "mRNA 2:"
print mRNA2

aminoseq1 = cd.translate_sequence(mRNA1)
aminoseq2 = cd.translate_sequence(mRNA2)

# Debug
print "Amino Sequence 1:"
print aminoseq1
print "Amino Sequence 2:"
print aminoseq2

sequence_comparison.compare_sequences(aminoseq1, aminoseq2, args.outfile)
