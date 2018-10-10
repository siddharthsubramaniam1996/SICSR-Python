import os
import re

filename = "/etc/passwd"
file = open(filename, "r")
for line in file:
   s = re.search('^([^:]*).*:([^:]*)',line)
   
#^([^:]*).*:([^:]*)
   
   print (line)
