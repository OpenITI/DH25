# Write a script that will detect OCR errors in a text, sort the errors and non-errors into specific lists and print the number of errors
# You need to fill in the relevant parts of the code indicated by the comments

# The errors in the text are as follows:
# 1. ا is mistranscribed as I
# 2. ل is mistranscribed as J
# 3. س is mistranscribed as w

# This is the path to the file containing the mistranscribed lines
path = 'data/mistranscribed_lines.txt'

# Open the file and read its contents as a list of lines


# Create a list of indices (so that you can give the line numbers)

# Initialize empty lists to hold the errors and non-errors

# Initialise the counters for each type of error

# Loop through the indices and do the following:
# 1. Print the index (line number)
# 2. Fetch the line corresponding to the index
# 3. Count the number of I errors and record them
# 4. Count the number of J errors and record them
# 5. Count the number of w errors and record them
# 6. If there are errors, append the line to the errors list (remember you should only append the line once, even if it has multiple types of errors)
# 7. If there are no errors, append the line to the non-errors list

# After the loop print the number of errors and non-errors and the number of each type of error
