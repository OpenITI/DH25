"""This script counts how many times a word appears in a text.

NB: please run the download_text.py script first
to download the text we're going to count words in.

The script uses the string method `count` to count how many times
a given string contains a given sub-string.

E.g.,
"This is an example".count("a")         # result: 2
"This is an example".count("example")   # result: 1
"This is an example".count("is")        # result: 2 (in "This" and "is")
"This is an example".count("Is")        # result: 0 (case-sensitive!)

Exercises:
0. Run the script and look at the output. Does it run without an error?
1. Take a look at the code. In which line do we tell Python what word to count?
2. Adapt the script to count how many times the word 'Black'
   (with capital B) is mentioned in the text and run it again.
   Do you get the same number as for 'black' with lowercase b?
3. Put the following comments in the right place in the script:
# load the text file into Python
# tell Python which word you want to search for
# define which text you want to search in
# count the number of times the word is in the text
4. Think of at least two ways how you could get the total count
   for both the lowercase and the uppercased version of the word
   (even if you don't have any idea how to implement your solution in Python)
5. One (naive) way to get the total count is to search for both words
   and to sum the two counts. Change the script to implement this.
"""

# VARIABLE ASSIGNMENT

# 
word = "black"

# 
filename = "frankenstein.txt"

# PROCESSING

# 
with open(filename, encoding="utf-8") as file:
    text = file.read()

# 
n_times = text.count(word)

# OUTPUT

print(f"The word {word} appears {n_times} times in {filename}")
