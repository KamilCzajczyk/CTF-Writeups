# Heal CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Heal** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Heal). 
---

we see open ports 22 and 80

![scn](imgs/scn.png "scn")

we need to add `heal.htb` to /etc/hosts

after scanning vhosts we found `api.heal.htb` 

![ff](imgs/ff.png "ff")

we see that application uses Ruby on Rails 

![ra](imgs/ra.png "ra")

after checking the website we see login form, we also can register new account

![rb](imgs/rb.png "rb")

we see some pdf builder

![rbb](imgs/rbb.png "rbb")

![rbbb](imgs/rbbb.png "rbbb")

![pd](imgs/pd.png "pd")

we can check our profile, we see that we created user that isnt admin

![ac](imgs/ac.png "ac")

if we choose survey we see another vhost `take-survey.heal.htb`

we can capture the requests after clicking `Export as PDF` and we see filename parameter that might be vulnerable to LFI

![rq](imgs/rq.png "rq")

![et](imgs/et.png "et")

it works we have file inclusion, from /etc/passwd we know about users: root, ralph, ron

![n](imgs/n.png "n")

there isnt any ssh key, we need to find config files. first config file that i found was: `../../config/application.rb`

![aa](imgs/aa.png "aa")

![a](imgs/a.png "a")

there is also `../../config/database.yml`, from this file we now about database path `../../storage/development.sqlite3`

![d](imgs/d.png "d")

![db](imgs/db.png "db")

![sq](imgs/sq.png "sq")

we can save it to .sqlite3 file to browse the data, we got password hash for `ralph`

![hs](imgs/hs.png "hs")

now we can use hashcat to crack it 

```
hashcat -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

![hc](imgs/hc.png "hc")

now we can login as ralph, we can also login into Limesurvey as ralph

![ras](imgs/ras.png "ras")

![ls](imgs/ls.png "ls")

![p](imgs/p.png "p")

we can check the limesurvey version, this version is vulnerable to Authenticated RCE, we can use this repo the create the attack `https://github.com/TheRedP4nther/limesurvey-6.6.4-authenticated-rce`

![rc](imgs/rc.png "rc")

we have access as www-data

![rs](imgs/rs.png "rs")

in some configuration file `/var/www/limesurvey/application/config/config.php` i found another password

![pw](imgs/pw.png "pw")

with this new password we can login to ssh as ron, we can also grab user flag

![us](imgs/us.png "us")

from linpeas output we see some open ports, after using curl on localhost:8500 we see `Moved Permanently`

![po](imgs/po.png "po")

![por](imgs/por.png "por")

now we can forward the port to our machine using ssh, we see `Consul 1.19.2` instance

![co](imgs/co.png "co")

if we google the version and exploit we see metasploit module

![ex](imgs/ex.png "ex")

we can try to execute it 

![rt](imgs/rt.png "rt")

we got root shell and root flag

# MACHINE PWNED
