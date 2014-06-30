#!/usr/bin/python	-tt
#	parseCSV.py

import os
import sys
import csv
import re

def searchCSV(csvFileName):
    try:
       fileSearch = open(csvFileName,'r')
       fileFound = fileSearch.read()

       try:
           searchString = input("Enter A Search String: ")
           match = re.search(searchString,fileFound)
           print(match.group(), "\nThe Search String: <",searchString,"> :Has Been Found")
       except AttributeError:
           print("The Search String: <",searchString,"> :Has Not Been Found") 

    except IOError:
      print('file input(%s) is not *.csv file' %s)
      print('2_searchCSV() call...')


    fileSearch.close()
  
def main():
    searchCSV(sys.argv[1])

if __name__ == '__main__':
   main()
