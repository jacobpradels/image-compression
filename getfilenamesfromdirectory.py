'''
Get all file names within a file folder
'''

mypath ='C:\\Users\\codye\\Documents\\Schoolwork\\Modernization Class'

from os import walk
files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    break
