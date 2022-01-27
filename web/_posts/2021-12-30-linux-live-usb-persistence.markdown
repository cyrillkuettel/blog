---
title: "Linux Live System"
layout: post
date: 2021-12-30 22:10 # yyyy-mm-dd
tag: 
- linux
image: https://raw.githubusercontent.com/cyrillkuettel/blog/gh-pages/assets/images/live-usb-linux.webp
headerImage: true
projects: true
hidden: true # don't count this post in blog pagination
description: ""
category: project
author: cyrill
externalLink: false
---

# What is this?
A live system is a bootable computer installation including operating system which runs directly form a storage device into a computer's memory. 

# Computers

I work on two computers. A laptop and a PC at home. Because I use them for the same work, they share a lot of the same software and configuration. This naturally introduces redundancy. Why? Because both systems have a nearly identical set of software installed. This means if you 
install new software, I always had to go throught the process twice. And on top of that the additional quirk of having to maintain two machines.They should preferably also as identical as possible, to avoid the "it works on my machine" moment. I decided to abandon this workflow altogether. I have therefore used a fresh, quite unconventional approach to solve this issue. I always use the live system. 

# Idea
It is obvious that the simple solution is to only use _one_ operating system. This is exactly what I started doing at the beginning of this year. I've installed my primary OS [MX Linux](https://mxlinux.org/) on a portable SSD. You can also use fast USB-Stick. If the installation is successful, it is possible to boot the operating system from the external storage medium. I find this quite amazing. During the boot process, you can select the option to persit all data. This will save files to your USB drive and the data will persist even after shutting down the live session.

## Advantages and disadvantages of using Linux persistence?
### Advantages
- Independence – The storage space used for persistent changes is independent of and separated from the OS
- Portability – Bookmarks, settings, system preferences, customizations and file downloads can in most cases be stored and retrieved when booting from different or multiple machines.
- More available storage space – Since the Live Linux Operating System is compressed with most persistent installs, the entire operating system takes up less space.
- Very fast boot up time.

### Disadvantages
- The main drawback I've encountered is that it is not possible to use systemd on a MX-live system. For me this is not a big problem. However, some services might not work without it (like VPN's for example).
- I don't know if system wide kernel updates work in this setup. I have not tested it. 

