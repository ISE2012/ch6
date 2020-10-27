# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:08:05 2020

@author: xyz
"""


def main():
    input = open("carroll.txt")
    longest = ""
    for line in input:
        if len(line) > len(longest):
            longest = line
    
    print("Longest line =", len(longest))
    print(longest)
main()
