"""This is a script that takes one page of text exported from eScriptorium (in plain
text format) and counts the number of words in it.

The first lines of the script (that open the file as a list of lines) have been written 
for you. You need to complete the rest of the script.

Remember that the code required is just the same as that covered during the class exercise."""

# Set the path to the file (change this to your own file path)

file_path = 'data/sample_page_arabic.txt'

# Open the file and read its contents into a list of lines
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Print the lines (to check that the file has been read correctly)
print(lines)

# Write a script below that does the following:
# 1. Initializes a variable to keep track of the total word count (set it to 0)
# 2. Loops through each line in the list of lines
# 3. For each line, splits the line into words
# 4. Counts the number of words in the line
# 5. Prints the number of words in the line (e.g. 'This line has X words')
# 6. Adds the number of words in the line to the total word count
# 7. At the end prints the total number of words