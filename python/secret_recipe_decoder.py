#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.amount} {self.description}"
        
#def decode_string(str):
def decode_string(encoded_string):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    # TODO: implement me 
    return ''.join(ENCODING.get(char, char) for char in encoded_string)
#    return '1 cup'



#def decode_ingredient(line):
#    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # TODO: implement me
#    return Ingredient("1 cup", "butter")

def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    amount, encoded_description = line.split('#')
    decoded_description = decode_string(encoded_description.strip())
    converted_amount = decode_string(amount.strip())
    return Ingredient(amount.strip(), decoded_description)


#def main():
#    """A program that decodes a secret recipe"""
    # TODO: implement me
def main():
    """A program that decodes a secret recipe"""
    input_file = 'secret_recipe.txt'
    output_file = 'decoded_recipe.txt'
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line:  # Ensure the line is not empty
                ingredient = decode_ingredient(line)
                outfile.write(f"{ingredient}\n")
    
if __name__ == "__main__":
    main()
