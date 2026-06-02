import re 
import shutil

text = input("Enter the given text : ")

email_formats = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_formats,text)

print("ALL emails in the file : ")
for i in emails:
    print(emails)