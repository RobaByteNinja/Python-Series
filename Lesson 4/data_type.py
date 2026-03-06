# String data type

# literal assignment
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
