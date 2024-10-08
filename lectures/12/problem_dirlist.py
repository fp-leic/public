#
# Lecture 12 - Recursion
# 
# 1) Create a recursive data structure representing a diretory tree
# 2) Pretty-print the diretory tree 
#
#  A *diretory tree* is either:
#  - a single file represented by its path (a string);
#  - a diretory represented by a pair (path, list of children)
#    where children are sub-trees 
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


def get_dirtree(path):
    """Build a directory tree. Wrapper function: 
    just calls the recursive function with empty prefix."""
    return get_dirtree_rec(path, '')


def get_dirtree_rec(path, prefix):
    '''Return the diretory tree for a prefix plus path.'''
    # check if we should recurse
    fullpath = os.path.join(prefix, path)
    if os.path.isdir(fullpath):
        entries = []
        for subpath in get_dirlist(fullpath):
            entries.append(get_dirtree_rec(subpath, fullpath))
        return (path, entries)
    else:
        return path


def print_dirtree(tree):
    '''Pretty print a dirtree; wrapper function.''' 
    return print_dirtree_rec(tree, '')
    
def print_dirtree_rec(tree, prefix):
    '''Pretty print a dirtree; worker function.'''
    
    if type(tree) is str:
        # base case (single file)
        print (prefix + tree)
    else:
        # recursive case: pair of dirname, entries
        (dirname, entries) = tree
        print (prefix + dirname)
        for subtree in entries:
            print_dirtree_rec(subtree, prefix + "|  ")
        

    
            
        
    
