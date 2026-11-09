def format_name(f_name, l_name):
    # Below this is a docstring (the code in green which you can use as a multi-line comment too)
    """take a first and last name and format it
    into
    a return the title case
    version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

a = """How was your day?"""
print(a)
print(formatted_name)  