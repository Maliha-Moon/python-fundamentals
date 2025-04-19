"""
String Indexing, Slicing, and Formatting
"""

# String declaration variants
a = 'moon'  # single quoted
b = "moon"   # double quoted
c = '''moon''' # triple quoted

# string indexing is accessing or extracting individual characters/elements
#📌 [-1] = index count from the end

#slicing
name = 'Maliha'
nameShort = name[1:3]
print(nameShort)

# negative slicing 
# name = 'M    a    l   i     h     a'
#       [-6] [-5] [-4] [-3] [-2] [-1]
print(name[-4:-1])

# advance slicing
print(name[:4]) # [: = [0: -> same as [0:4]
print('length = ', len(name))
print(name[1:]) # :] = :length] -> same as [1:5]

# Traverse backward slicing
text = "DataScience"
print(text[::-1])

# 📌f string -> format string
print(f"Good Afternoon {name}")


"""
Search and Replace Operations
"""

# replace() chaining
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Maliha").replace("<|Date|>","11 April 2025"))

# find()
# detect double space
greet = "Moon is a girl"
print(greet.find("  ")) # -1 means not found!
greet2 = "Moon is a  girl"
print(greet2.find("  ")) # return the index

# replace the double space with single space
print(greet2.replace("  "," "));
print(greet2)  #📌 strings are immutable which means you cannot change them by running functions on them

# format with escape sequence
letter = "hello Moon,\n\t This is python.\n Thanks"
print(letter)


"""
Split, join and strip
"""

# split() = breakes the string into list of words
song = "The rain in spain...."
print(song.split()); # by default,any no. of whitespace is the word boundary
print(song.split("n")) # delimeter can be used to specify word boundary, delimeter doesn't appeare in the result
# extract the domain part
email = "user@example.com"
domain = email.split("@")[1] #📌 split() returns list. here, ['user','example.com']. So, [0]=user, [1]=example.com
print(f"domain: {domain}")

# join() = opposite of split() which creates string from list of words with the glue
color = ["red","green","blue"]
glue = " "
print(color)
print(glue.join(color))

# strip() = remove leading (from the beginning) and trailing (ending) whitespaces 
wrd= "   hello moon  "
print(wrd.strip())

# Given a messy string of product reviews:
reviews = "5 stars,Great product!|1 star,Poor quality.|4 stars,Good value."
# Parse this into a structured dictionary format:
# {
#   "5 stars": "Great product!",
#   "1 star": "Poor quality.",
#   "4 stars": "Good value."
# }
print(f"{reviews.split('|')[0]} \n {reviews.split('|')[1]} \n {reviews.split('|')[2]}")
