---
title: "Pythonic Adapter"
layout: post
date: 2022-07-10 00:35  # yyyy-mm-dd
tag: 
- python
headerImage: false
externalLink: false
category: blog
author: cyrill
description: Using the adapter Pattern
---
 
This is a nice example showcasing the adapter pattern and how to transform code into more beautiful and readable python code.


So, we got some code here, fairly short. What does it do? 
Well we've got a series of imports from a sdk that knows how to talk to a routing device.
It makes a connection to the devices. It gets the routing table, but if the routing table is missing it logs and exception and it does a clean up.
This particular connection, if you don't clean up on the way out can leave the router in a state that's hard to log back into.
So there's some nice handling there. 
Then it loops over the routes and prints a short little report of all the routes, with corresponding names and their
IP addresses.
And then at the end it commits any changes, does a cleanup and disconnects

Is this code beautiful? No.   
Is beautiful better than ugly? Yes.   

There's nothing very wrong with this code, it works, and it's readable.

{% gist cyrillkuettel/6d7ffc6f6c37c8148b0affb76ba1af37 %}

Now look at this code:

{% gist cyrillkuettel/ce24b6565e33b1c1bc65edf5b32d6be5 %}

This code does the same thing. Which code is better, the one on the top or the second one? The second one of. 
There's only one problem, this code doesn't run. It won't work. (But other than that, it's really good code.)   
Why won't it work? We need to write an adapter. We need to transform this api one that would work with this code.

Well written python code looks like business logic. When you're doing setup and tear-down logic, you should build a 
context manager so that you can use a `with` statement. Where there are packages, you should make a single module that makes 
it easier to import everything so that the code can become beautiful.

Where somebody is getting the number of elements, looping over a range, and looking up something by index. 

- Define a `__len__`
- There's a way in python to get something by index, it's called square brackets. And it's quite nice.  In other languages, like Java or C++, if you write a class that does not have getters and setters, you're incompetent. Getters and setters are not necessary in python. If you need to change access to the attributes of a class later, you can add properties.

{% gist cyrillkuettel/c5aec00827ed590d33414e057d42b299 %}


This is the adapter. What it's going to do is wrap the underlying object. 
Some notes on `NetworkElement` class:

- Get in the habit of putting `__repr__` on your classes, it makes debugging so much easier.
- Add custom exceptions, this is useful documentation for the people that use the api.
- Separate the exception handling from the business logic. ("push it down")
- We put a `@property` on the routing_table. This enables us to do direly access the attribute in the second code snippet.
- The setup and tear-down logic: We have created magic functions: `__enter__` and `__exit__`. This enables us to use the
`with` keyword. 
- Look at the `__repr__` in the NetworkElement. We don't hardwire the name of the class, we use `self.__class__.__name__`   
 This is good technique. Why would you do that? Sub-classing.

Notes on `RoutingTable` class:
Once something has a `__getitem__` and a `__len__` it's called a Sequence in python. And all Sequences are _iterable_. 
Which means now, we can run a for loop on it.     

Other notes on making code pythonic.
- Choose good function names and variable names.
- Name the parameters, especially if it's a complex function. This makes the code more readable.
- Use named tuples to improve readability of code. (`from collections import namedtuple?`)

Source: [Raymond Hettinger - Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015]( https://www.youtube.com/watch?v=wf-BqAjZb8M)
