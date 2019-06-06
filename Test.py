import re
r = re.compile(r"^\d*[.,]\d*$")
if r.match('1,32'):
    print ('it matches!')
