import os
import string
import re
import json
passwords = json.loads(open('Password.json').read())
arr = []
for password in passwords:
    arr+= password
