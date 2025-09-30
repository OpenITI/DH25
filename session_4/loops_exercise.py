"""This script has already been written for you, but it contains a number of errors. It is your job to find and fix them.

The script is supposed to take a text file that has been mistranscribed by an OCR system (it has transcribed Latin in the place of Arabic
characters) identify the mistakes, and print the lines and the nature of the error. Another loop counts the total errors for the entire text.

There are three known types of Latin character errors: mistranscriptions of characters as 'J', 'I and 'w'."""

# The path to the file with the erroneous transcription (do not change)
file_path = "data/mistranscribed_lines.txt"

# The code that reads in the file as lines
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Errors in the script begin from here:

for line in lines:
    
print(Checking line:, lines)
errors = ""
if 'J' in line:
    error += "J "

if 'I' in line:
    error += "I "

if 'w' in line:
    error += "w "


print(Erroneous characters:, errors)
print("-----")

j_errors = 0
i_errors = 0
w_errors = 0


for line in lines:
    j_count = lines.count('J')
    j_errors = j_count

    i_count = lines.count('I')
    i_errors = i_count

    w_count = lines.count('w')
    w_errors = w_count

    print("Total J errors:", j_errors)
    print("Total I errors:", i_errors)
    print("Total w errors:", w_errors)