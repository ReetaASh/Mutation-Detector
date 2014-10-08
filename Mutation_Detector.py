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
# Last modified: 10/7/2014

import argparse

import central_dogma

parser = argparse.ArgumentParser()
parser.add_argument("infile1", help="file containing the first sequence " +
                    "in FASTA format", type=str)
parser.add_argument("infile2", help="file containing the second sequence " +
                    "in FASTA format", type=str)
parser.add_argument("--outfile", help="Filename for the output file", type=str)
parser.parse_args()

infile1, infile2 = args.infile1, args.infile2
outfile = ""
if args.outfile:
    outfile = args.outfile

# Read in sequences from FASTA files
# Ignore first line since that's just header info, not part of the sequence
lines1 = lines2 = []
sequence1 = sequence2 = ""
with open(infile1, 'r')
    lines1 = infile1.readlines()[1:]
with open(infile2, 'r')
    lines2 = infile2.readlines()[1:]
for line in lines1:
    sequence1 += line
for line in lines2:
    sequence2 += line

# TODO: Program code here satisfying requirement 1 of the assignment
