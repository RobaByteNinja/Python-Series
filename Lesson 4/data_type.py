# String data type

# literal assignment
import math
first = 'Murad'
last = 'Alamudin'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
burger = str("cheese")
print(' ')
print(type(burger))
print(type(burger) == str)
print(isinstance(burger, str))

# Concatenation
print(' ')
fullname = first + ' ' + last
print(fullname)

fullname += '!'
print(fullname)

# Casting number to string
print(' ')
decade = str(1980)
print(type(decade))
print(decade)

statement = 'I like rock music from the ' + decade + 's.'
print(statement)

# Multiline
multiline = '''
Hey, how are you?                                   

I was just checking in.    
                                All good?

'''
print(multiline)

# Escaping special character
sentence = 'I\'m at work\tHey!\n\nwhere\'s this at \\located'
print(sentence)

# String Methods
print(' ')
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)

print(len(multiline))
multiline += '                               '
multiline = '           ' + multiline
multiline = multiline + '                   '
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Tea".ljust(16, '.') + "$2".rjust(4))
print("Milk".ljust(16, ".") + "$3".rjust(4))
print("mango".ljust(16, ".") + "$2".rjust(4))
print(' ')

# String index
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some method return boolean data
print(first.startswith('D'))
print(first.startswith('M'))
print(first.endswith("D"))
print(first.endswith('d'))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type

# integer data type
price = 100
best_price = int(100)
print(type(price))
print(isinstance(best_price, int))

# float data type
gpa = 3.26
y = float(3.26)
print(type(gpa))
print(isinstance(y, float))

# complex data type
comp_value = 3 + 2j
print(type(comp_value))
print(comp_value.imag)
print(comp_value.real)

# Built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(81))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zip_code = "3000"
zip_code_number = int(zip_code)
print(type(zip_code_number))

# Error if you attempt to cast incorrect data
location = 'Adama'
or_location = int(location)
print(or_location)
