# Jerry CTF - HackTheBox Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Jerry** CTF challenge on [HackTheBox](https://app.hackthebox.com/machines/Jerry). 
---

we see open port 8080

![nm](imgs/nm.png "nm")

we see tomcat webpage

![tc](imgs/tc.png "tc")

to get to /manager we need to login

![lh](imgs/lh.png "lh")

if we cancel the are given hints for a default credentials

![cl](imgs/cl.png "cl")

we can use default credentials tomcat:s3cret to see admin dashboard, we can upload our own code

![sh](imgs/sh.png "sh")

crafting reverse shell payload with msfvenom

![pa](imgs/pa.png "pa")

we got hit with reverse shell

![rs](imgs/rs.png "rs")

we can grab both flags

![fl](imgs/fl.png "fl")

# MACHINE PWNED
