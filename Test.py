import re
r = re.compile(r"^\d*[.,]\d*$")
if r.match('1,32'):
    print ('it matches!')

j = re.compile(r'^\d*$')

if j.match('70'):
    print("GOOD")
