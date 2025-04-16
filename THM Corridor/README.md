# Corridor CTF - TryHackMe Room
# **!! SPOILERS !!**
#### This repository documents my walkthrough for the **Corridor** CTF challenge on [TryHackMe](https://tryhackme.com/room/corridor). 
---


we see open port 80 

![scn](imgs/scn.png "scn")

on the website we see a picture with doors that we can click

![d](imgs/d.png "d")

in the source code we see a image map with diffrent long values that look like hashes

![map](imgs/map.png "map")

they are indeed md5 and they go from 1 to 13, so we can see a pattern

![c](imgs/c.png "c")

we know about potential IDOR so we can follow the pattern and fuzz other locations

we can use ZAP proxy and choose numbers from 0 to 1000, then we can add a processor to create md5 hash of the number value and then try to access an endpoint

![z5](imgs/z5.png "z5")

![ff](imgs/ff.png "ff")

we found 15 responses with 200 OK status codes, the original map contains 13 endpoints

![co](imgs/co.png "co")

in endpoint with hash representing 14 there is nothing interesting

![n](imgs/n.png "n")

in endpoint with hash representing 0 there is a flag

![f1](imgs/f1.png "f1")

# FLAG OBTAINED
