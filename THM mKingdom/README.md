# mKingdom CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **mKingdom** CTF challenge on [TryHackMe](https://tryhackme.com/room/mkingdom). 
---


we only see one open port 85

![scan](imgs/scan.png "scan")

scanning with feroxbuster we see `/app` directory

![ferox1](imgs/ferox1.png "ferox1")

after clicking the button we are redirected to `/app/castle`, afer scanning again and checking Wappalyzer we know that website uses `Concrete CMS 8.5.2`

![ferox](imgs/ferox.png "ferox")

there is a login page, i used admin:password and it worked we have access to dashboard

by going to `System & Settings -> Files -> Allowed File Types` we are able to add .php to allowed file types

![ext](imgs/ext.png "ext")

i then created folder called shell then went to `Files -> Upload File` and uploaded pentestmonkey reverse shell 

![fm](imgs/fm.png "fm")

![up](imgs/up.png "up")

site generated our link
`http://10.10.22.186:85/app/castle/application/files/2817/4189/9056/shell.php ` and now we just need to access it

it worked we have reverse shell as www-data

![www](imgs/www.png "www")

in `/var/www/html/app/castle/application/config` there is database.php file containing credentials

![pass](imgs/pass.png "pass")

we can use that to login as user `toad`


linpeas found PWD_token encoded in base64 that translates to 
`...[REDACTED]...`

![lin](imgs/lin.png "lin")

linpeas also found SUID for /bin/cat

![suid](imgs/suid.png "suid")

i used this string to switch to user `mario` 

![mario](imgs/mario.png "mario")

i copied pspy64 to victim and found hidden cronjob executed by root

![ps](imgs/ps.png "ps")

now we need to do few things, first changing /etc/hosts to point to our IP (if you want to edit with nano you need stable shell)

![hosts](imgs/hosts.png "hosts")

then create `app/castle/application` in there we create `counter.sh` file with simple reverse shell, then starting python server remembering about changing port to 85,then we just wait for connection (victim will automatically grab malicious file from our server)

![serv](imgs/serv.png "serv")

we got root shell

![root](imgs/root.png "root")

now we can grab root and user flag

![flags](imgs/flags.png "flags")

# MACHINE PWNED
