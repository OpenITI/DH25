"""Use this script as a base for evaluating OCR outputs. It contains one function error_rate that takes two lines of text: reference and hypothesis
and calculates the cer or wer depending on the approach specified

An example with two lines of text has been provided.

Start by running the code to see the output, then proceed with the exercises"""

import numpy as np
import re

# Functions to be used - do not worry about normalise_utf - that is a function that is used by error_rate

def normalise_utf(reference, hypothesis, normalisation_table = {}):
    """Normalise cases where a mixture of Persian and Urdu keyboard has been
    used to one Persian variant
    Used to reduce exagerated error rates
    Normalises both sides of the relationship: reference and hypothesis
    Uses a normalisation table specified as a dicts, which records exchanges
    e.g. {"ك" : "ک"} would switch an Arabic Kaf for a Persian kaf, where
    the key is the letter to be exchanged and the value is the letter to exchange (note 
    text direction likely to flip)
    """
    for base_char in normalisation_table.keys():
        normalisation = normalisation_table[base_char]

        reference = re.sub(base_char, normalisation, reference)
        hypothesis = re.sub(base_char, normalisation, hypothesis)
    
    return reference, hypothesis


def error_rate(reference, hypothesis, approach="cer"):
    """Whole function (except condition for wer versus cer) taken from
    https://www.geeksforgeeks.org/assessing-nlp-model-effectiveness-wer-crt-and-sts/"""
    
    # Apply normalisation function
    reference, hypothesis = normalise_utf(reference, hypothesis)

    if approach == "wer":
        reference = reference.split()
        hypothesis = hypothesis.split()
    
    # Quick fix for empty input data - 0 either string or list is empty
    if len(reference) == 0 or len(hypothesis) == 0:
        return 0
    
    # Initializing the matrix
    d = np.zeros((len(reference)+1, len(hypothesis)+1), dtype=np.uint32)
    for i in range(len(reference)+1):
        d[i][0] = i
    for j in range(len(hypothesis)+1):
        d[0][j] = j

    # Computing WER
    for i in range(1, len(reference)+1):
        for j in range(1, len(hypothesis)+1):
            if reference[i-1] == hypothesis[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            d[i][j] = min(d[i-1][j] + 1,                    # Deletion
                          d[i][j-1] + 1,                    # Insertion
                          d[i-1][j-1] + substitution_cost)  # Substitution
    
    
    return d[len(reference)][len(hypothesis)] / len(reference)


# Example usage of the function. Note that to get wer you need to specify approach as "wer"

reference_string = "It was considered well preserved, and was pronounced by Murphy, who gives a design of it in his book of travels, to be one of the most beautiful relics of Roman architecture in the world. As yet there has been no explanation vouchsafed by the authorities. So let Murray, Bradshaw, Baedeker, and others, strike out the Tower of Sertorius, one of the glories of Evora, from the list of the sights of Portuguese travel."
hypothesis = "It was considered well preserved, and was pronounced by Murphy, who gives a design of it in his book of travels, to be one of the most beautiful relics of Roman archi­tecture in the world.As yet there has been no explanatioa vouchsafed by tbe authori­ties. So let Murray, Bradahaw, Biedeker and others strike out the Tower of Setsr­iiu, one of the glt-ries of Evora, from the list of Hie sights of Portuours? travel."

cer = error_rate(reference_string, hypothesis)
wer = error_rate(reference_string, hypothesis, approach="wer")

print(f"The character error rate for the pair is: {cer}")
print(f"The word error rate for the pair is: {wer}")

# Now add code that takes txt files and applies the function to real data
