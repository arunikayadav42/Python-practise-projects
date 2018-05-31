import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
no = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: '+no.group())