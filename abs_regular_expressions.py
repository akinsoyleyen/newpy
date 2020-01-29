import re

text = "Trying out the numbers 333"

phone_num_regex = re.compile(r'\d\d\d')
print(phone_num_regex.findall(text))