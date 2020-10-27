# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:00:01 2020

@author: xyz
"""


def main():
    print ("This program creates a file of usernames from a")
    print ("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')
    
    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create a username
        uname = (first[0]+last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()