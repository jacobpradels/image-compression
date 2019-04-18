'''
Get all file names within a file folder
'''

#mypath ='C:\\Users\\codye\\Documents\\Schoolwork\\Modernization Class'
def pathtolist(pathname):
    '''Function takes a copied path file directory and converts it so 
    python can read and pull file names'''
    new_path = pathname.split('\\')
    com_path = ''
    for string in new_path:
        com_path += (string + '\\')

    from os import walk
    files = []
    for (dirpath, dirnames, filenames) in walk(com_path):
        files.extend(filenames)
        break
    return files