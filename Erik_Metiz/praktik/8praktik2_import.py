# 8.15
# from printing_functions import *       (можно всё или по отдельности)
from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.16
import functions_get_formatted_name

my_name = functions_get_formatted_name.get_formatted_name('viktor', 'lyutikov')
print(my_name)

# ---------------------------------------
from functions_get_formatted_name import get_formatted_name
your_name = get_formatted_name('diman', 'lebedos')
print(your_name)

# ---------------------------------------
from functions_get_formatted_name import get_formatted_name as format
name = format('sergey', 'kireev', 'sanovich')
print(name)

# ---------------------------------------
import functions_get_formatted_name as ff
nn = ff.get_formatted_name('forest', 'ichpachmakovich')
print(nn)

# ---------------------------------------
from functions_get_formatted_name import *
my_mew_format = get_formatted_name('niki', 'lyutik')
print(my_mew_format)