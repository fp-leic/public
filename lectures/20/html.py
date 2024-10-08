#
# A sample module for generating HTML
# Pedro Vasconcelos, 2023
# Note: this is a bit simplistic; do *not* attempt to use it in production!
#
import functools

#
# An HTML element has the form "<TAG> .... </TAG>"
#
def element(tag, *args):
    if len(args) == 0: 
        # special case with empty args: <tag/>
        return "<"+tag+"/>"
    else:
        # general case
        return "<"+tag+">" + ' '.join(args) + "</"+tag+">"


# Some common HTML elements; special cases of the above
p = functools.partial(element, 'p')   # paragraph
ol = functools.partial(element, 'ol') # ordered list
li = functools.partial(element, 'li') # list item
hline = element('hline')              # horizontal line (no arguments)

if __name__ == '__main__':
    print('This file is a library - it should be imported')        
        
