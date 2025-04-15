# Mr Robot CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Mr Robot** CTF challenge on [TryHackMe](https://tryhackme.com/room/mrrobot). 
---

we see open ports 80 and 443

![scn](imgs/scn.png "scn")

there is a lot of content on the website, we can check the robots.txt

![r](imgs/r.png "r")

we found 2 hidden files `fsocity.dic` and `key-1-of-3.txt`

![f1](imgs/f1.png "f1")

![d](imgs/d.png "d")

using gobuster to enumerate hidden folders

![go](imgs/go.png "go")

the most interesting one is /wp-login suggesting the use of WordPress, using wpscan to enumerate users but it doesnt seem to work

if we try to login manually we see the error: Invalid username

![er](imgs/er.png "er")

we can try to use the dictionary file we found to test for potential username

after using ZAP to fuzz the username we see that there could be users: elliot and Elliot

![fu](imgs/fu.png "fu")

there is a hint `There's something fishy about this wordlist... Why is it so long?` so i checked how many lines are unique, there are 11451 unique line (it is better than all 858160 lines)

```
sort fsocity.dic | uniq | wc -l
```

![wc](imgs/wc.png "wc")

so now we can modify the wordlist to make it smaller

```
sort fsocity.dic | uniq > uniq.txt
```

now if we try to login as elliot we see other error about wrong password for our user (we fuzzed working user)

![el](imgs/el.png "el")

now after fuzzing the password we found one request that gives 302 status code so it could be a working password

![fu2](imgs/fu2.png "fu2")

now we are logged to wordpress dashboard

![pa](imgs/pa.png "pa")

looking for ways to upload reverse shell file, we can use Appearance -> Editor and use 404.php, then we copy code and save the file

![404](imgs/404.png "404")

then we can go to `http://IP/tttt` and we should get our shell

we got shell as daemon

![rv](imgs/rv.png "rv")

we can look around /home folder, we see robot user, we also see the second flag but we dont have permissions to read it, but we can read some md5 hash that looks like robot password

![h](imgs/h.png "h")

we can use crackstation to crack it

![c](imgs/c.png "c")

now we have access as robot and we can grab second flag

![rb](imgs/rb.png "rb")

after running linpeas, we know about SUID for nmap

![lin](imgs/lin.png "lin")

we can check GTFObins for PE factor

![gt](imgs/gt.png "gt")

now we need to run nmap in interactive mode and execute a command to spawn a shell as root

```
$ /usr/local/bin/nmap --interactive
nmap> !sh
```

now we have root access and last flag

![rt](imgs/rt.png "rt")

# MACHINE PWNED
