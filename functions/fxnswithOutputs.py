# return statement replaces the output of the 

def format_name(f_name, l_name):
    """Take a first name and last name and formats it 
        to return title case version of the name"""
    if f_name == "" or l_name == "":
        return ""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("ANgEla", "yU")

# functions with more than one return statements 