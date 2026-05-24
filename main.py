
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


#regex patterns (5)
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
url_pattern = r"\b(?:https?://|www\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"
phone_pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{3,4}[-.\s]?){2,3}\d{0,4}\b"
card_pattern = r"\b(?:\d[ -]*?){13,16}\b"
currency_pattern = r"\b(?:USD|RWF|\$)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b"

#extract data using regex
emails = re.findall(email_pattern, raw_txt)
urls = re.findall(url_pattern, raw_txt)
phone_numbers = re.findall(phone_pattern, raw_txt)
credit_cards = re.findall(card_pattern, raw_txt)
currency_amounts = re.findall(currency_pattern, raw_txt)

#alu email validation
alu_official_emails = []
alu_alumni_emails = []
alu_si_emails = []

for email in emails:
    if email.endswith("@alueducation.com"):
        alu_official_emails.append(email)
    elif email.endswith("@alumni.alueducation.com"):
        alu_alumni_emails.append(email)
    elif email.endswith("@si.alueducation.com"):
        alu_si_emails.append(email) 


# Mask credit card numbers before saving
masked_credit_cards = []

for card in credit_cards:
    masked_card = hide_card_number(card)

    if masked_card is not None:
        masked_credit_cards.append(masked_card)


# Store all results in a dictionary
results = {
    "emails": remove_repetitions(emails),
    "alu_official_emails": remove_repetitions(alu_official_emails),
    "alu_alumni_emails": remove_repetitions(alu_alumni_emails),
    "alu_si_emails": remove_repetitions(alu_si_emails),
    "urls": remove_repetitions(urls),
    "phone_numbers": remove_repetitions(phone_numbers),
    "credit_cards_hidden": remove_repetitions(masked_credit_cards),
    "currency_amounts": remove_repetitions(currency_amounts),
    "security_note": "Credit card numbers are hidden before output. invalid and suspicious text is ignored unless it matches safe regex rules"
}

#save json results
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)


#print a simple success message
print("+++ EXTRACTION SUCCESSFULLY COMPLETE ++++")
print("Results saved to output/output.json")