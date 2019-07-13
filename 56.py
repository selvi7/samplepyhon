import re
print(bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', 'hasAlphanum123')))
print(bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)', 'some string')))