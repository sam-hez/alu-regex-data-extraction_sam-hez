# Regex Data Extraction and Validation Assignment
## How to Run 
```text
python main.py
```

## Output
output is saved as JSON. It contains extracted emails, ALU emails, URLs, phone numbers, masked credit cards, and currency amounts.
Even though the input file contains other text like times, HTML tags, and hashtags, the program only extracts the five data types listed above.


## Folder Structure

```text
alu-regex-data-extraction_sam-hez/
├── input/
│   └── raw-text.txt
├── output/
│   └── sample-output.json
├── main.py
└── README.md
```


## Project Overview

This project is a simple Python program that reads raw text from a file and extracts useful structured data using regular expressions.
I used Python because it is simple and readable for this type of text processing task.

The regex patterns were kept practical and understandable, while still handling realistic variations such as different phone number formats, URLs, currency values, and card number spacing. the program works with messy, realistic text that looks like data from support tickets, student records, payment messages, and external API logs. 