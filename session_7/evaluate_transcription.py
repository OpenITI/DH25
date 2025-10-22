"""Use this script as a base for evaluating OCR outputs.

It contains one function `error_rate` that takes two lines of text:
reference and hypothesis (that is, ground truth and OCR transcription)
and calculates the CER (character error rate)
or WER (word error rate) depending on the approach specified.

An example with two lines of text has been provided.

Start by running the code to see the output, then proceed with the exercises.

Exercise 1: Check the error rate of your own manual transcription:
a. Export the `instructors_correction` and `students_correction` transcription layers
for the page in which you corrected the transcription in eScriptorium
(export as datatype TEXT)
b. Save the instructors_correction layer in this folder as "groundtruth.txt"
c. Save the students_correction layer in this folder as "student.txt"
d. in this script, load both text files
e. calculate the error rate between the ground truth and transcription.

Exercise 2: Compare the error rates of different automatic transcription:
a. create a subfolder in this folder called with your name:
b. Export all of the following transcription layers for your page:
  - `all_arabic_scripts`
  - `apt20221130`
  - `gen2-print-n7m5-union-ft_best`
  - `39_from_pretrain_2_best_urdu`
c. In your script, use a loop to compare the error rates
   of each of these automatic transcriptions with the ground truth.
"""

import numpy as np

# Provide a list that defines characters
# that need to be replaced with other characters
# (to be used in the `normalise` function):
normalisation_table = [
    # NORMALISE DIFFERENT VERSIONS OF ARABIC LETTERS:
    ["ك", "ک"],     # ARABIC LETTER KAF > ARABIC LETTER KEHEH [Persian kaf]
    ["ں", "ن"],     # ARABIC LETTER NOON GHUNNA > ARABIC LETTER NOON 
    ["ة", "ه"],     # ARABIC LETTER TEH MARBUTA GOAL > ARABIC LETTER HEH  
    ["ھ", "ه"],     # ARABIC LETTER HEH DOACHASHMEE > ARABIC LETTER HEH
    ["ہ", "ه"],     # ARABIC LETTER HEH GOAL > ARABIC LETTER HEH
    ["ۃ", "ه"],     # ARABIC LETTER TEH MARBUTA GOAL > ARABIC LETTER HEH 
    ["ە", "ه"],     # ARABIC LETTER AE > ARABIC LETTER HEH 
    ["ى", "ی"],     # ARABIC LETTER ALEF MAKSURA > ARABIC LETTER FARSI YEH 
    ["ي", "ی"],     # ARABIC LETTER YEH > ARABIC LETTER FARSI YEH 
    ["ے", "ی"],     # ARABIC LETTER YEH BARREE > ARABIC LETTER FARSI YEH

    # REMOVE VOWELS:
    ["ً", ""],       # ARABIC FATHATAN > delete  
    ["ٌ", ""],       # ARABIC DAMMATAN > delete
    ["َ", ""],       # ARABIC FATHA > delete
    ["ُ", ""],       # ARABIC DAMMA > delete
    ["ِ", ""],       # ARABIC KASRA > delete
    ["ْ", ""],       # ARABIC SUKUN > delete
    ["ٰ", ""],       # ARABIC LETTER SUPERSCRIPT ALEF > delete

    # REMOVE MADDA:
    ["ٓ", ""],       # ARABIC MADDAH ABOVE > delete 
    ["آ", "ا"],     # ARABIC LETTER ALEF WITH MADDA ABOVE > ARABIC LETTER ALEF

    # NORMALISE HAMZAS:
    ["ئ", "ئ"],     # ARABIC LETTER YEH + ARABIC HAMZA ABOVE > ARABIC LETTER YEH WITH HAMZA ABOVE
    ["ئ", "ئ"],     # ARABIC FARSI LETTER YEH + ARABIC HAMZA ABOVE > ARABIC LETTER YEH WITH HAMZA ABOVE
    ["ىٔ", "ئ"],     # ARABIC LETTER ALEF MAKSURA + ARABIC HAMZA ABOVE > ARABIC LETTER YEH WITH HAMZA ABOVE
    ["ؤ", "ؤ"],     # ARABIC LETTER WAW + ARABIC HAMZA ABOVE > ARABIC LETTER WAW WITH HAMZA ABOVE
    ["ۂ", "ه"],     # ARABIC LETTER HEH GOAL WITH HAMZA ABOVE> ARABIC LETTER HEH 
    ["أ", "ا"],     # ARABIC LETTER ALEF WITH HAMZA ABOVE > ARABIC LETTER ALEF
    ["ٔ", ""],       # ARABIC HAMZA ABOVE > delete
    ["إ", "ا"],     # ARABIC LETTER ALEF WITH HAMZA BELOW > ARABIC LETTER ALEF
    ["ٕ", ""],       # ARABIC HAMZA BELOW > delete

    # REMOVE NON-STANDARD ARABIC SYMBOLS:
    ["ـ", ""],      # ARABIC TATWEEL > delete
    ["؁", ""],      # ARABIC SIGN SANAH > delete 
    ["؂", ""],      # ARABIC FOOTNOTE MARKER > delete 
    ["؎", ""],      # ARABIC POETIC VERSE SIGN > delete 
    ["ؐ", ""],       # ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM > delete 
    ["ؑ", ""],       # ARABIC SIGN ALAYHE ASSALLAM > delete 
    ["ؔ", ""],       # ARABIC SIGN TAKHALLUS > delete
    ["۔", "."],     # ARABIC LETTER FULL STOP > FULL STOP
    ['‌', ""],       # ZERO WIDTH NON-JOINER > delete
    ['‍', ""],       # ZERO WIDTH JOINER > delete
    ["ﷲ", "الله"],     # ARABIC LIGATURE ALLAH ISOLATED FORM > (separate letters)
    ["٭", "*"],     # ARABIC FIVE POINTED STAR > ASTERISK
    
    # NORMALISE ALL DIGITS TO "WESTERN" ARABIC DIGITS:
    ["٠", "0"],     # ARABIC-INDIC DIGIT ZERO > DIGIT ZERO
    ["١", "1"],     # ARABIC-INDIC DIGIT ONE > DIGIT ONE
    ["٢", "2"],     # ARABIC-INDIC DIGIT TWO > DIGIT TWO
    ["٣", "3"],     # ARABIC-INDIC DIGIT THREE > DIGIT THREE
    ["٤", "4"],     # ARABIC-INDIC DIGIT FOUR > DIGIT FOUR
    ["٥", "5"],     # ARABIC-INDIC DIGIT FIVE > DIGIT FIVE
    ["٦", "6"],     # ARABIC-INDIC DIGIT SIX > DIGIT SIX
    ["٧", "7"],     # ARABIC-INDIC DIGIT SEVEN > DIGIT SEVEN
    ["٨", "8"],     # ARABIC-INDIC DIGIT EIGHT > DIGIT EIGHT
    ["٩", "9"],     # ARABIC-INDIC DIGIT NINE > DIGIT NINE
    ["۰", "0"],     # EXTENDED ARABIC-INDIC DIGIT ZERO > DIGIT ZERO
    ["۱", "1"],     # EXTENDED ARABIC-INDIC DIGIT ONE > DIGIT ONE
    ["۲", "2"],     # EXTENDED ARABIC-INDIC DIGIT TWO > DIGIT TWO
    ["۳", "3"],     # EXTENDED ARABIC-INDIC DIGIT THREE > DIGIT THREE
    ["۴", "4"],     # EXTENDED ARABIC-INDIC DIGIT FOUR > DIGIT FOUR
    ["۵", "5"],     # EXTENDED ARABIC-INDIC DIGIT FIVE > DIGIT FIVE
    ["۶", "6"],     # EXTENDED ARABIC-INDIC DIGIT SIX > DIGIT SIX
    ["۷", "7"],     # EXTENDED ARABIC-INDIC DIGIT SEVEN > DIGIT SEVEN
    ["۸", "8"],     # EXTENDED ARABIC-INDIC DIGIT EIGHT > DIGIT EIGHT
    ["۹", "9"],     # EXTENDED ARABIC-INDIC DIGIT NINE > DIGIT NINE
]

# Functions to be used - do not worry about normalise - that is a function that is used by error_rate

def normalise(text, mapping):
    """Normalise a text by replacing some characters by others.

    Normalisation is used to score the models in a fairer way.
    For example, if the model identified a letter as an Arabic kaf,
    but the ground truth has a Persian letter kaf, we might not
    want to penalize it for that - since they are basically the same.

    A `mapping` list that maps characters that need to be replaced,
    to the characters by which they need to be replaced,
    needs to be provided."""
    
    for character, normalised_character in mapping:
        text = text.replace(character, normalised_character)
    return text



def error_rate(reference, hypothesis, normalisation_mapping=[], approach="cer"):
    """Calculate the error rate of a transcription when compared to a hypothesis.

    The error rate is defined as the number of errors divided by the number of characters/words.
    
    This function is based on:
    https://www.geeksforgeeks.org/assessing-nlp-model-effectiveness-wer-crt-and-sts/

    Args:
        reference (str): the ground truth text
        hypothesis (str): the transcription
        normalisation_mapping (list): list of characters that need to be normalised
        approach (str): either "cer" (character accuracy rate)
            or "wer" (word error rate)
    """
    
    # Normalise both inputs:
    reference = normalise(reference, normalisation_mapping)
    hypothesis = normalise(hypothesis, normalisation_mapping)

    # shortcuts for empty input strings:
    if len(reference) == 0 :
        if len(hypothesis) == 0:
            # If both the hypothesis and reference are empty,
            # the error rate is by definition 0%:
            return 0
        else:
            # if only the reference is empty,
            # the error rate is by definition 100%:
            return 1

    # split both strings into words if you want to calculate word error rate (wer):
    if approach == "wer":
        reference = reference.split()
        hypothesis = hypothesis.split()
    
    # Initialize a matrix of zeros
    # (number of rows = number of characters/words in the reference text,
    #  number of columns = number of characters/words in the hypothesis text):
    d = np.zeros((len(reference)+1, len(hypothesis)+1), dtype=np.uint32)

    # Compute the edit distance between the reference and the hypothesis,
    # character / word by word:
    for i in range(len(reference)+1):    # first row
        d[i][0] = i
    for j in range(len(hypothesis)+1):   # first column
        d[0][j] = j
    for i in range(1, len(reference)+1): # all other cells
        for j in range(1, len(hypothesis)+1):
            if reference[i-1] == hypothesis[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            d[i][j] = min(d[i-1][j] + 1,                    # Deletion
                          d[i][j-1] + 1,                    # Insertion
                          d[i-1][j-1] + substitution_cost)  # Substitution

    # the edit distance is the bottom right cell of the matrix:
    edit_distance = d[len(reference)][len(hypothesis)]

    # calculate the error rate:
    error_rate = edit_distance / len(reference)
    
    return error_rate


# Example usage of the function. 

reference  = "امّا بعد اين کلمات چند تحریر افتاد در معنی مطلب آنکه غرض از گفتن" # NB: the Persian variants of kaf and yeh are used here
hypothesis = "اما بعد اين كلمات جند تحریر افتاد در معنی مطلب آنكه غرض از كفت"  # NB: the Arabic variants of kafs and yehs are used here

# calculate the character error rate:
cer = error_rate(reference, hypothesis)
# calculate the word error rate:
wer = error_rate(reference, hypothesis, approach="wer")

print(f"The character error rate for the pair (without normalisation) is: {cer}")
print(f"The word error rate for the pair (without normalisation) is: {wer}")

# now recalculate the error rates with normalisation:
cer = error_rate(reference, hypothesis, normalisation_table)
wer = error_rate(reference, hypothesis, normalisation_table, approach="wer")

print(f"The character error rate for the pair with normalisation is: {cer}")
print(f"The word error rate for the pair with normalisation is: {wer}")


# Now add code that takes txt files and applies the function to real data






