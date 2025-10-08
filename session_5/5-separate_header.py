"""This script separates the metadata header from the body of a text.

1. take a look at the text file you're working with
   and identify where the metadata header ends and the body begins
2. initialize two variables, one for the header and one for the body;
   at the start, they should be empty strings
3. Loop through the lines in the text and add the lines that belong
   to the header to your header variable, and the lines that belong
   to the body to your body variable.
   (how are we going to do this?)
"""

filename = 

# PROCESSING

# 
with open(filename, mode = "r", encoding="utf-8") as file:
    lines = file.readlines()
