"""
File: Project 12
Author: Cole Crase
This program allows the user to inputs a filename
and prints to the terminal a report of the wages paid
to the employees for the given period. The report
will be in tabular format with the employee's name,
the hours worked, and the wages paid for that period.
"""

inputFileName = input("Input filename: ")
inputFile = open(inputFileName, "r")
count = 1
for line in inputFile:
   newLine = str(count).rjust(1, " ") + "> " + line
   print()
   print("  <last name>    <hourly wage>    <hours worked>")
   print(newLine) 
   count += 1 
