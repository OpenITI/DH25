"""This script downloads a text from the Project Gutenberg library.

We tell Python at which URL we can find the text,
and which filename we want to give to the downloaded text.

Exercises:
0. Run the script and look at the output. Can you find the downloaded file
   on your computer?

1. Take a look at the code. In which lines do we tell
   Python where to find the file online, and how to name the downloaded file?

2. Insert the following comments at the correct place in the script:
# save the downloaded text with the filename you specified:
# display a message to confirm the download:
# store the URL of the text and the filename in variables
# import a library that contains functions for downloading from the internet
# pass the link to the text to Python and tell it to download it

3. Adapt the script to download another text:
   address of the new text: https://raw.githubusercontent.com/OpenITI/RELEASE/v2023.1.8/data/0001ImruQaysIbnHujr/0001ImruQaysIbnHujr.Diwan/0001ImruQaysIbnHujr.Diwan.JK007512-ara1
   filename of the new text: Diwan_ImrulQays.txt

4. To define a string in Python, you can use double or single quotation marks.
   Replace the double quotation marks in the `url` variable assignment
   with single quotation marks and rerun the script. Did it still work?

5. What happens if you don't use any quotation marks at all
   around the `url` variable? Try removing the quotation marks and rerunning the script.

6. You can choose your own variable names.
   Change the variable name `url` to `link` and rerun the script.
   NB: if you change the variable name in the variable assignment,
   you need to change it everywhere in the script!

7. Change the variable name `filename` to another meaningful variable name,
   and rerun the script. Did it still work?

8. Ask ChatGPT how to get the current time in Python, and store
   the current time in a variable. Then add that variable to the output message,
   so that the script prints at the end "Finished downloading at "
   (followed by the currrent time).
"""

# IMPORTS

# 
import requests

# VARIABLE ASSIGNMENT

# 
url = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
filename = "frankenstein.txt"

print("downloading", url)
print("->", filename)

# PROCESSING

#  
text = requests.get(url).text

# OUTPUT

# 
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

# 
output_message = f"Saved {url} as {filename}" 
print(output_message)
