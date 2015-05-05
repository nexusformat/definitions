#!/usr/bin/env python

# Tested under both python2 and python3.

'''
merging all .part files in the directories passed as arguments to create a new 
input file for xsltproc. 
'''

from __future__ import print_function
import os, sys, re,os.path

part_file_pattern = re.compile(r".*\.part$")

def get_part_files(directory):
    return [f for f in os.listdir(directory) if part_file_pattern.match(f)]

def print_file(filename):

    with open(filename,"r") as in_file:
        for line in in_file:
            print(line)


#print header of output
print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
print("<definitions>")

for directory in sys.argv[1:]:
    file_list = get_part_files(directory)
    
    for filename in file_list:
        print_file(os.path.join(directory,filename))

#print the footer of the output
print("</definitions>")


