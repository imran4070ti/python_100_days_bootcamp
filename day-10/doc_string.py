def format_name(fname, lname):
    '''
        fname = First Name
        lname = Last Name
    '''
    if fname == "" or lname == "":
        return "Invalid inputs"
    else:
        return f'{fname.title()} {lname.title()}'
    

formated_name = format_name('imRaN', 'hAsAN')
print(formated_name)