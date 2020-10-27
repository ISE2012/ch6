# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:48:39 2020

@author: xyz
"""


def main():
    input = open("workerHours.txt")
    for line in input:
        id, name, mon, tue, wed, thu, fri = line.split()
        # cumulative sum of this employee's hours
        hours = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)
        print(name, "ID", id, "worked", hours, "hours: ", hours/5, "/ day")

main()

