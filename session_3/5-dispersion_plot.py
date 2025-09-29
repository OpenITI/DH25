"""This script creates a dispersion plot, which shows where in a text
one or more specified words are mentioned.

This script uses the plotly library; install it first:
- Windows: pip install plotly
- Mac: pip3 install plotly
"""

# IMPORTS

import re
import plotly.express as px


# VARIABLE ASSIGNMENT

# tell Python which word you want to search for:
word = input("Which word do you want to search in the text? ")

# define which text you want to search in:
filename = "frankenstein.txt"

# PROCESSING

# load the text file into Python:
with open(filename, encoding="utf-8") as file:
    text = file.read()

# count the number of characters in the text
# (we'll need this to show where the words are found
# in relation to the beginning and end of the work):
text_length = len(text)

# find where each word is mentioned in the text:
locations = [match.start() for match in re.finditer(word, text)]

# OUTPUT

# create a scatter plot of all locations in which the word is mentioned:
fig = px.scatter(x=locations, y=[word]*len(locations), title=word)
# add a vertical line to indicate the end of the book:
fig.add_vline(text_length)
# display the graph in the browser:
fig.show()


        





