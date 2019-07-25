#!/usr/bin/python3
print("content-type:text/html; charset-UTF-8\n")

import re 

def clean_text(text):
    cleaned_text = re.sub('[n]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+@\#$%&\\\=\(\'\"]','',cleaned_text)
    return cleaned_text

read_file = open('./menu.txt', 'r')
write_file = open('./menu_clean.txt', 'w')
text = read_file.read()
text = clean_text(text)
write_file.write(text)
read_file.close()
write_file.close()
