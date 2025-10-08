"""This script finds the context a word appears in a text.

NB: please run the download_text.py script first
to download the text we're going to count words in.


Exercises:
0. Run the script and look at the output. Does it run without an error?
1. Copy the following comments to the correct place in the script:
# load the text file into Python and split it into lines
# tell Python which word you want to search for
# loop through the lines and print the line if it contains the word
# define which text you want to search in
2. Adapt the script to also count how many times the word 
   is mentioned in the text and run it again.
3. Highlight the search word in the line by surrounding it with two asterisks,
   like this: "In the **black** night, the stars shone brightly"
   (which string method are you going to have to use?)
3. Print not only the actual text of the line that contains the word,
   but also the line number
   (you will need a variable to keep track of the line number)
"""

# VARIABLE ASSIGNMENT

#
word = "black"

#
filename = "frankenstein.txt"

# PROCESSING

#
with open(filename, encoding="utf-8") as file:
    lines = file.readlines()

#
for line in lines:
    if word in line:
        print(line)

