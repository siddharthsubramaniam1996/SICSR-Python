import os
import sys

directory = input ("input directory here :")

for filename in os.listdir(directory): # parse through file list in the current directory

	if filename.find("_") > 0: # if an underscore is found

		newfilename = filename.replace("_"," ") # convert underscores to space's

		newfilename.lower() # convert to lower case

		os.rename(filename, newfilename) # rename the file
