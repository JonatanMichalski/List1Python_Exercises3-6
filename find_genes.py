# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:56:59 2026

@author: jonas
"""

def find_genes(sequence):
    """Find potential genes in a DNA sequence.

    A gene starts with the start codon ATG and ends with the first
    stop codon (TAG, TAA, or TGA) in the same reading frame.
    The gene length must be a multiple of three, and no stop codons
    may occur between the start and end codons.

    Args:
        sequence (str): DNA sequence containing bases A, T, C, and G.

    Returns:
        list[str]: A list of potential genes found in the sequence.
            Each gene includes its start and stop codons.

    Raises:
        TypeError: If sequence is not a string.
        ValueError: If sequence contains invalid DNA bases.

    Preconditions:
        - sequence is a string.
        - sequence contains only A, T, C, and G.

    Postconditions:
        - Every returned gene starts with ATG.
        - Every returned gene ends with TAG, TAA, or TGA.
        - Every returned gene has a length divisible by three.
        - No intervening stop codons occur within a returned gene.

    """
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be a string.")

    sequence = sequence.upper()
    valid_bases = {'A', 'T', 'C', 'G'}
    
    if any(base not in valid_bases for base in sequence):
        raise ValueError("Sequence can contain only A, T, C, and G characters.")
        
    #define start and stop codons
    start_codon = "ATG"
    stop_codons = {"TAG", "TAA", "TGA"}
    
    genes = []
    i = 0
    
    #search for start and stop codons
    for frame in range(3):
        i = frame
        while i <= len(sequence) - 3:
            #search for start codon in current frame
            if sequence[i : i + 3] == start_codon:
                j = i + 3
                #scan downstream codons in the same frame
                while j <= len(sequence) - 3:
                    codon = sequence[j : j + 3]
                    if codon in stop_codons:
                        #valid gene found
                        genes.append(sequence[i : j + 3])
                        #move index past the stop codon to avoid overlapping genes in same frame
                        i = j + 3
                        break
                    j += 3
                else:
                    #no stop codon found for this start codon in current frame
                    i += 3
            else:
                i += 3

    return genes

from list1 import dna_complement

if __name__ == "__main__":
    from list1 import dna_complement

    try:
        # get the DNA sequence from the user
        dna = input("Enter a DNA sequence: ").strip()

        # searching in the original sequence
        original_genes = find_genes(dna)
        
        # searching in the complementary sequence
        comp_dna = dna_complement(dna)
        comp_genes = find_genes(comp_dna)

        print("\nOriginal DNA sequence:", dna.upper())
        print("Genes in the original sequence:")
        if original_genes:
            for gene in original_genes:
                print(" -", gene)
        else:
            print(" No genes found.")

        print("\nComplementary DNA sequence:", comp_dna)
        print("Genes in the complementary sequence:")
        if comp_genes:
            for gene in comp_genes:
                print(" -", gene)
        else:
            print(" No genes found.")

    except (TypeError, ValueError) as error:
        print("Error:", error)