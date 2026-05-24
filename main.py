
import re
import json
import os

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