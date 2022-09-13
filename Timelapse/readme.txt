NOTE: before running this code you will have to add 'timelapse.htb' to your hosts file.
Example from kali: echo '<target ip>  timelapse.htb' | sudo tee -a /etc/hosts

Not a stable edition(works for me), might encounter problems with value 'x'(line 10). If you are facing problems try running the pase1 command(line7) in terminal, get the password returned(last block of string), and replace the value of 'rpass'(line 11) with the password.

Tested only on Kali Linux
coded by vanishyi
