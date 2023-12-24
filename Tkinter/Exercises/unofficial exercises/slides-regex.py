import re
# program to match only lowercase letters joined by underscores
text='aa_a'
if re.match(r'^[a-z]+_[a-z]+$',text):
    print('ye')
else:
    print('n')
