# use lambda expressions in place of a function that has only return statement
# variable = lambda argument_list: return_expression

dirr = lambda obj: [at for at in dir(obj) if not at.startswith('_')]
square = lambda x: x*x
line = lambda ch='-',size=80: print(ch*size)


def remove_names_starting_with(names, start_str):
    for name in names.copy():
        if name.startswith(start_str):
            names.remove(name)