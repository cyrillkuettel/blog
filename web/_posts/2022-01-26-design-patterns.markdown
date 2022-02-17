---
title: "Design Patterns"
layout: post
date: 2022-01-26 03:33
tag: books
headerImage: false
projects: true
hidden: true # don't count this post in blog pagination
description: "test"
category: project
author: cyrill
externalLink: false
---

I've always liked to read. Usually, I prefer to read fiction. From time to time, I do read books about programming, software development and various topics surrounding this area. For my latest book, I decided to pick up Design Patterns: Elements of reusable object-oriented software.     


<div class="side-by-side">
    <div class="toleft">
        <img class="image" src="/assets/images/design_patterns.webp" alt="">
    </div>

    <div class="toright">
        <p>
A lot of elegant solutions in software can be reduced to the same patterns. In a lot of cases it boils down to a few techniques. 
I decided to read this book because I read a lot about it. It's over twenty years old, but still relevant today. 
I'm on page 10, and I can already sense this is not going to be a quick read. However, I'm certain I can learn a lot from this book. 
So let's get started then!</p>
    </div>
</div>

# Summary
I will summarize this book. First write down notes by hand. Only then retype it on the computer. I have found this to be an effective technique. This ensures that you only write down things that really matter.

The first chapter talks about object-oriented design in a general sense. Most of this stuff is not new to me, but it's still useful to read about it. 
This paragraph resonated especially well with me:
> Strict modeling of the real world leads to a system that reflects today's realities but not necessarily tomorrow's. The abstractions that emerge during design are key to making a design flexible. 

We are talking about polymorphism here. I think polymorphism can be compared to the plug-and-play concept. It lets an object make few examples about other objects beyond supporting a particular interfaces. Polymorphism decouples objects from each other and lets them vary their relationship to each other at runtime. 

> Program to an interface, not an implementation.

> Favor composition over inheritance. 

<div class="side-by-side">
    <div class="toleft">
        <img class="image" src="/assets/images/aggregation_composition.drawio.png.webp" alt="">
    </div>

    <div class="toright">
        <p>
            `composition` vs `aggregation`. Two concepts that are easily confused.
            Delegation is a way of making composition as powerful for reuse as inheritance. 
        </p>
    </div>
</div>

### Runtime structure
Trying to understand the runtime strucutre of a program is like trying to understnad the dynamism of living ecosystems from static taxonomy of plants and animals. 

### Other approaches:
Encapsulate the concept that varies. Consider what should be variable in your design. 