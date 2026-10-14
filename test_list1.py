# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:11:25 2026

@author: jonas
"""

import unittest
from list1 import divisible, common, subsets, random_walk, dna_complement
from find_genes import find_genes

class TestList1(unittest.TestCase):
    # Tests for task 1
    def test_divisible_typical(self):
        self.assertEqual(divisible([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])
        self.assertEqual(divisible([10, 15, 20, 25], 5), [10, 15, 20, 25])

    def test_divisible_boundary(self):
        self.assertEqual(divisible([], 3), [])
        self.assertEqual(divisible([1, 2, 4], 3), [])

    def test_divisible_exceptions(self):
        with self.assertRaises(TypeError):
            divisible("not a list", 2)
        with self.assertRaises(TypeError):
            divisible([1, "2", 3], 2)
        with self.assertRaises(TypeError):
            divisible([1, 2, 3], 2.5)
        with self.assertRaises(ValueError):
            divisible([1, 2, 3], 0)
            
    # Tests for task 2
    def test_common_typical(self):
        self.assertEqual(common([7, 5, 2, 1, 8, 5, 6, 8], [8, 6, 8, 3, 4, 5, 2]), [5, 2, 8, 6, 8])

    def test_common_boundary(self):
        self.assertEqual(common([], [1, 2, 3]), [])
        self.assertEqual(common([1, 2, 3], []), [])
        self.assertEqual(common([1, 2], [3, 4]), [])

    def test_common_exceptions(self):
        with self.assertRaises(TypeError):
            common("abc", [1, 2])
        with self.assertRaises(TypeError):
            common([1, 2], None)
            
    # Tests for task 3
    def test_subsets_typical(self):
        result = subsets({1, 2})
        expected = [set(), {1}, {2}, {1, 2}]
        self.assertEqual(len(result), 4)
        for sub in expected:
            self.assertIn(sub, result)

    def test_subsets_boundary(self):
        self.assertEqual(subsets(set()), [set()])

    def test_subsets_exceptions(self):
        with self.assertRaises(TypeError):
            subsets([1, 2, 3])
        with self.assertRaises(TypeError):
            subsets("abc")
            
    # Tests for task 4
    def test_random_walk_typical(self):
        coords = random_walk(2)
        self.assertEqual(coords[0], (0, 0))
        #check that the last coordinate is strictly further than n from origin
        last_x, last_y = coords[-1]
        self.assertGreater((last_x**2 + last_y**2)**0.5, 2)

    def test_random_walk_boundary(self):
        coords = random_walk(0)
        self.assertGreater(len(coords), 1)

    def test_random_walk_exceptions(self):
        with self.assertRaises(ValueError):
            random_walk(-1)
        with self.assertRaises(TypeError):
            random_walk("10")
            
    # Tests for task 5
    def test_dna_complement_typical(self):
        self.assertEqual(dna_complement("ATCG"), "CGAT")
        self.assertEqual(dna_complement("AAAA"), "TTTT")

    def test_dna_complement_boundary(self):
        self.assertEqual(dna_complement(""), "")

    def test_dna_complement_exceptions(self):
        with self.assertRaises(TypeError):
            dna_complement(1234)
        with self.assertRaises(ValueError):
            dna_complement("ATCGU")  #invalid base
            
    # Tests for task 6        
            
    def test_find_genes_typical(self):
        #sequence with 1 propper gene ATG CTT TGA
        seq = "CCATGCTTTGAAC"
        self.assertEqual(find_genes(seq), ["ATGCTTTGA"])

        #sequence with two propper genes in the same reading frame
        seq_two = "ATGAAATAGCCCATGGCGTGA"
        self.assertEqual(find_genes(seq_two), ["ATGAAATAG", "ATGGCGTGA"])

    def test_find_genes_boundary(self):
        #no start/stop codon
        self.assertEqual(find_genes("ATGCGCTCA"), [])
        self.assertEqual(find_genes("CCCCTAGGA"), [])
        
        #empty sequence
        self.assertEqual(find_genes(""), [])

        #stop codon before start codon
        self.assertEqual(find_genes("TAGATGAAATGA"), ["ATGAAATGA"])

    def test_find_genes_exceptions(self):
        #type error
        with self.assertRaises(TypeError):
            find_genes(12345)
        
        #invalid base
        with self.assertRaises(ValueError):
            find_genes("ATGCTTXGA")
            
if __name__ == "__main__":
    unittest.main()