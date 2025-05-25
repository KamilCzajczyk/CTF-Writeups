# Photobomb CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Photobomb** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Photobomb). 
---

we see open ports 22 and 80

![scn](imgs/scn.png "scn")

from websiter source code we see intersting file `photobomb.js` and `/printer` route 

![sc](imgs/sc.png "sc")

the /printer is protected with basic HTTP auth

![pw](imgs/pw.png "pw")

in js file wee see some credentials that might work

![js](imgs/js.png "js")

they worked and we can access /printer

![pr](imgs/pr.png "pr")

if we capture the request that is send while clicking "Download photo to print" we see 3 parameters: photo, filetype, dimensions

if we try to manipulate those parameters we can simply find that filetype paramter is vulnerable to command injection

we can use payload `png;sleep+5`, the response takes much longer than standard one, we have Blind command injection, we dont see the result (if we use `png;id`) but we know that command is being executed because the system is stalling

![ci](imgs/ci.png "ci")

![cierr](imgs/cierr.png "cierr")

we can now create the payload that will send reverse shell to us

![rs](imgs/rs.png "rs")

![pr](imgs/pr.png "pr")

we got reverse-shell access as wizard and we can grab user flag

![us](imgs/us.png "us")

we can run linpeas

![sudol](imgs/sudol.png "sudol")

from linpeas we see that we can run sudo on some script `/opt/cleanup.sh` with SETENV

we can inspect the cleanup.sh code

![cl](imgs/cl.png "cl")

we see that find command is run without absolute path so we can create our own malicious version of it 

```
$ cd /tmp
$ mkdir find && cd find
$ nano find

--
Content of the file:
cp /bin/bash /tmp/bashroot && chmod +s /tmp/bashroot
--

$ chmod +x find
```

![fi](imgs/fi.png "fi")

now we can run this command to execute our malicious script as root user to copy the /bin/bash with SUID

```
sudo PATH=/tmp/find:$PATH /opt/cleanup.sh
```

![sd](imgs/sd.png "sd")

it worked now we use `/tmp/bashroot -p` to gain root shell

we got root access and root flag

![rt](imgs/rt.png "rt")

# MACHINE PWNED
