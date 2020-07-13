"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["sweet"] = "a way to express chill satisfaction or affirmation"
word_definitions["dope"] = "a way to express chill and enthusiastic appreciation"
word_definitions["chill"] = "a way that you should be most of the time"
word_definitions["cereal"] = "the one food I could eat the rest of my life, no problem"
word_definitions["connie's"] = "home of the best chicken biscuit with gravy you've ever tasted -- and don't get me started on the blueberry doughnuts"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["chill"])
print(word_definitions["connie's"])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key, value in word_definitions.items():
    print(f'The definition of "{key}" is: {value}')
