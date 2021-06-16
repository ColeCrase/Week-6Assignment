"""
File: Project9
Author: Cole Crase
This script is to create a program listing from a source program.
The user is to input the names of two files, and the script
output the file, numbering each line as it goes.
"""

inputFileName = input("Input filename: ")
outputFileName = input("Output filename: ")
inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")
count = 1
for line in inputFile:
   newLine = str(count).rjust(4, " ") + "> " + line
   outputFile.write(newLine)
   print(newLine)
   count += 1 
