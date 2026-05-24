
import re #for using regex
import json #to save json output
import os #so we can work with file paths


#----------------------#

#function to read the raw txt file in out dir input/raw-text.txt
def read_input_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        return file.read()
    
#Function to remove repeated values & keep original order
def remove_repetitions(items):
    clean_list = []

    for item in items:
        if item not in clean_list:
            clean_list.append(item)

    return clean_list


# function to hide/mask credit card numbers for security purposes
def hide_card_number(card_number):
    digits_only = re.sub(r"\D", "", card_number)

    if len(digits_only) < 13:
        return None
    
    last_4 = digits_only[-4:]
    return "++++ ++++ ++++ " + last_4

#define file paths using os for raw txt & output json
input_file = os.path.join("input", "raw-text.txt")
output_file = os.path.join("output", "output.json")

#read raw text
raw_txt = read_input_file(input_file)
