#
# Lecture 13 - Recursion
# 
# Create a recursive data structure represeting a diretory tree
# Pretty-print the diretory tree 
#
# jlopes, pbv
#

import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def get_dirtree(path, prefix=""):
    '''Return the diretory tree for a path.
    A *diretory tree* is either:
    - a single file represented by its path;
    - a diretory represented by a pair (path, list of children)
      where children are sub-trees 
    Example:
    ("home", 
    [ ("Documents", 
      [ ("FP", ["lists.txt", "recursion.pdf", "functions.ipynb"]),
        ("Python", ["hello_world.py", "readme.md"])
      ]),
      ("Downloads", [
         ("Movies", [
          ("TV Series", ["BreakingBad.mp4", "TheBigBangTheory.avi"]),
           "1.avi", "22", "001.mp4" 
         ])
      ]),
     "tmp.txt", "page.html"])
    '''
    # check if we should recurse
    fullpath = os.path.join(prefix,path)
    if os.path.isdir(fullpath):
        entries = []
        for subpath in get_dirlist(fullpath):
            entries.append(get_dirtree(subpath, fullpath))
        return (path, entries)
    else:
        return path


def print_dirtree(tree, prefix=""):
    '''Pretty print a dirtree.'''
    
    if type(tree) is str:
        # base case (single file)
        print (prefix + tree)
    else:
        # recursive case: pair of dirname, entries
        (dirname, entries) = tree
        print (prefix + dirname)
        for subtree in entries:
            print_dirtree(subtree, prefix + "| ")
        

    
            
        
    
