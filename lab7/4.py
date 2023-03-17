def iFormattable(type_of):
    if type_of in (list, set, dict):
        return True
    return False


def is_it_formattable(x: object) -> bool:
    return iFormattable(type(x))


print("int 100: ", is_it_formattable(100))
print("list [100]: ", is_it_formattable([123, 12312]))
print("string '100': ", is_it_formattable("1231312"))
