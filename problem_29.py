# Problem 29: Function with default argument
# Find and fix the error

def add_to_list(item, lst=[]):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


