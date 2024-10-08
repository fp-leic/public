#
# NB16: Generating HTML text using higher-order functions
# Pedro Vasconcelos, 2023
#
import functools

#
# An HTML element has the form "<TAG> .... </TAG>"
#
def element(tag, *args):
    return "<"+tag+">" + '\n'.join(args) + "</"+tag+">"

# Some common HTML elements; special cases of the above
p = functools.partial(element, 'p')   # paragraph
ol = functools.partial(element, 'ol') # ordered list
li = functools.partial(element, 'li') # list item
hline = element('hline')              # horizontal line (no arguments)

example = p('This is an example list',
            ol(li('first item'),
               li('second item'),
               li('third item')),
            'This is the end of the list')
print(example)
print()

def shopping_list(shoplist):
    """Build HTML for a shopping list."""
    total = sum(price for item,price in shoplist)
    args = (li(f'{item}: {price} EUR') for item,price in shoplist)
    html = p('Shopping list:',
             ol(*args),
             hline,
             f'Total: {total} EUR')
    return html

fruits = [('Apples', 2.5), ('Strawberries', 4.5), ('Pinaples', 5.5)]
print(shopping_list(fruits))        
        
