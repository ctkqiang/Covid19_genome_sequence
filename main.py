#!/usr/bin/env python3 
# pip3 install biopython

import Bio
from Bio.Seq import Seq as sequence
from Bio import SeqIO 
from Bio.Data import CodonTable

version = Bio.__version__
genome_extension = "fasta"
genome_data_location = "Data/sequence.txt"
covid_sequence = sequence(genome_data_location)

standard_table = CodonTable.unambiguous_dna_by_id[1]


def main():
    print("Covid 19 Genome Sequnence Location: ", covid_sequence)

    for covid_sequence_record in SeqIO.parse(genome_data_location, genome_extension):
        print("Sequence Identity: " , covid_sequence_record.id)
        print("Sequence: " , repr(covid_sequence_record.seq))
        print("sequence Length: ", len(covid_sequence_record))
    return

    covid_sequence.translate(table="COVID Class 2", to_stop= True)

    return 

def data_table():
    print(standard_table)

if __name__ == "__main__":   
    print("Version: ", version)
    main()    
    data_table()
