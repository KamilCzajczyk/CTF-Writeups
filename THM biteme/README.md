# biteme CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **biteme** CTF challenge on [TryHackMe](https://tryhackme.com/room/biteme). 
---


we see open ports 22 and 80

![scn](imgs/scn.png "scn")

we see deafult apache page, from feroxbuster scan we get hidden `/console/` folder

![fer](imgs/fer.png "fer")

on the site we also see js function handleSubmit

![js](imgs/js.png "js")

i used chatGPT and dcode to deobfuscate the code 

![dcode](imgs/dcode.png "dcode")

![jj](imgs/jj.png "jj")

we see 

```
@fred I turned on php file syntax highlighting for you to review jason
```

if we google `php file syntax highlighting` we see a tip in php manual about a good way to handle the syntax highliting accessible via web browser

![cm](imgs/cm.png "cm")

we have file /console/index.php we can try `/console/index.phps`

![s](imgs/s.png "s")

and it works we see some php code, we see that the code includes functions.php, we can test if e can reach it or reach functions.phps

![func](imgs/func.png "func")

in this code there is include to config.php so we can again try config.phps

![conf](imgs/conf.png "conf")

now by using cyberchef and converting from hex we have a user: jason_test_account

![cc](imgs/cc.png "cc")

after looking at the code we need to find a password that after using md5 on it will produce 001 as last characters

here is simple python code to do that

![py](imgs/py.png "py")

now we need to complete multi-factor authentication with 4 digit code, we can try multiple times so we can use fuzzer to guess the correct digits (i use ZAP proxy)

![mfa](imgs/mfa.png "mfa")

we found odd looking response with 302 status code suggesting redirect correct code was 1121

![fuzz](imgs/fuzz.png "fuzz")

now we have access to file browser and file viewer

![da](imgs/da.png "da")

we can test file browser by inputing / and we see whole filesystem root folder

![fb](imgs/fb.png "fb")

we also have access to file viewer, we can test by using /etc/passwd

![fv](imgs/fv.png "fv")

we can users: fred and jason

![hm](imgs/hm.png "hm")

we can use this interface to find user flag

![f](imgs/f.png "f")

after looking around i found jason ssh private key in /home/jason/.ssh/id_rsa

![rsa](imgs/rsa.png "rsa")

![rsa2](imgs/rsa2.png "rsa2")

now we need do crack the passphrase

```
$ ssh2john key > hash.txt
$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

![j](imgs/j.png "j")

now we have user access !

![us](imgs/us.png "us")

checking the sudo -l output

![sudol1](imgs/sudol1.png "sudol1")

we are in sudo group by sadly we dont know the password, but we cas switch user to fred by using 

```
sudo -u fred /bin/bash
```

now as fred looking again at sudo -l output we see that we can execute `systemctl restart fail2ban`

![sudol2](imgs/sudol2.png "sudol2")

we can use this command to find fail2ban

```
find /lib/systemd /etc/systemd -name "fail2ban*"
```

there is 1 file writeable by fred `/etc/fail2ban/action.d/iptables-multiport.conf`

![ff](imgs/ff.png "ff")

now we can use `nano /etc/fail2ban/action.d/iptables-multiport.conf` to edit the file and change actionban to `actionban = cp /bin/bash /tmp && chmod 4755 /tmp/bash`

![ab](imgs/ab.png "ab")

then we restart the fail2ban service using `sudo systemctl restart fail2ban`, then we need to provoke the ban, we can use hydra like `hydra -l root -P rockyou.txt ssh://10.10.x.x`, after a few seconds we should see bash in /tmp folde with SUID

then we need to use `/tmp/bash -p`, now we have root access 

![bs](imgs/bs.png "bs")

we have root flag

![root](imgs/root.png "root")

# MACHINE PWNED
