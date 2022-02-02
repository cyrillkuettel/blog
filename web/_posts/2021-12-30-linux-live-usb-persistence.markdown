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

# Context

I work on two computers. I have both a laptop and a PC (tower) at home. Because I use them for the same work, they share a lot of the same software and configuration. This naturally introduces redundancy. So I have used two systems. They have a nearly identical set of software installed. Installing new software on one computer almost always required to install it on the other computer as well.
Having to maintain two machines, that are _almost_ but not quite identical, is not a pleasant experience. 

I used a fresh, rather unconventional approach for this problem. Rather than using a cloud-based solution, I literally use the same Operating System: A live system with persistence. 

# What's a live system`?
A live system is a bootable computer installation including operating system which runs directly form a storage device into a computer's memory. 

# Idea
I've installed my System of choice [MX Linux](https://mxlinux.org/) on a portable SSD. If I work on one computer, I can just boot form the (external) SSD. With persistence activated, all local files get stored on disk. The data persists even after shutting down the live session. I find this quite amazing.

## Advantages and disadvantages of using Linux persistence?
### Advantages
- Independence – The storage space used for persistent changes is independent of and separated from the OS
- Portability – Bookmarks, settings, system preferences, customizations and file downloads can in most cases be stored and retrieved when booting from different or multiple machines.
- Very fast boot up time.
- More available storage space – Since the Live Linux Operating System is compressed with most persistent installs, the entire operating system takes up less space.


### Disadvantages
- The main drawback I've encountered is that it is not possible to use systemd on a MX-live system. For me this is not a big issue. However, some services might not work without it. For example, an application might depend on the `systemctl` command. `Systemctl` is the main utility for managing system services under systemd. This command cannot be called in a live session, because a live sessions does not boot with systemd. It uses SysVinit. 
- I don't know if system wide kernel updates work in this setup. I have not tested it. 