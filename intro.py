# this is the first comment
spam = 1 #this is the second comment
text = "#this is not a comment becasue it's inside the qoute."
"""
print(spam)
print(text)
"""

#using python as calculator
# = is the assign sign for value assign to the variable
a, b = 2, 2

sum = a+b
dif  = a-b
mul  = a*b
div  = a/b

#print(sum, dif, mul, div)

#floar division with // operator
# % return the remainder
a = 17
b = 3
div = a/b
#print(div)
flor_div = a//b
#print(flor_div)

#python power with ** operator
a = 5
b = 2
#print(a ** b)

# MIND IT: in interactive mode last printed value can get with _(underscore) sign

#strings

str = "spam eggs"
str = "doesn\'t"
str = "Yes, \" they said."
str = "\"Yes,\" they said."
str = '"Isn\'t," they said.'
#print(str)

str = 'First line.\nSecond line.' # \n means new line
#print(str)

#print('C:\some\name')
#print(r'C:\some\name') #note  the r before the quote

# 3 times 'un', followed by 'ium'
str = 5 * 'un' + 'ium'
#print(str)

str = 'Py' 'thon'
#print(str)

text = ('Put several strings within parentheses '
        'to have them joined together.')
#print(text)
word = 'Python'
#print(word[0], word[5])

#print(word[-1], word[-2], word[-6])
# print the slice part of string

#print(word[0:2])
#print(word[2:5])

#print(word[:2]+ word[2:])
#print(word[:4]+word[4:])

text = 'J'+word[4:42]
text = word[:2]+ 'py'
#print(len(text))

# LIST ****

squares = [1, 4, 9, 16, 25]
#print(squares[-3:])

print(squares[:])
cubes = [1, 8, 27, 65, 125]




