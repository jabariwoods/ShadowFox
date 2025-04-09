def format_string(num, char):
    return "{} is represented as {} in octal".format(num, format(num, 'o'))

print(format_string(145, 'o'))
