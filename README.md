# ROS(2) Tutorials

Here is all the introductory resources that we use on the team for various software libraries.

# Python

https://www.codecademy.com/learn/learn-python (Requires Account)

https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/python-robotics/ (Requires Account)

## Installing Ubuntu

Many programs run only or run best on a Linux Kernel, while ROS has primary support only for Ubuntu.
So a Ubuntu 'installation' is highly recommended.
### Installation Via WSL
This is ideal if you are just learning this for the first time or checking out linux and are running Windows, then I would install wsl 2 with the link below
- https://www.windowscentral.com/how-install-wsl2-windows-10

Check out for a beginner guide with how to install wsl2 within Windows 10. Due to different circuimstances, GUI Components are not availible for WSL, however GPU acceleration
For installing WSLg, check out the following link
https://github.com/microsoft/wslg


### Installation Via VirtualBox
This is the last in terms of performance, but the GUI works well.

### Installation on Bare Metal

If you are installing on Bare Metal, resarch about installing on your laptop, as there can be oddities with each one, depending on the manufacturer.

#### Laptop Examples 
Previous members have had problems with Wi-Fi or Graphics on Linux. 
- One member had problems with HP laptops. 
- Configuring graphics with built-in graphics can be problematic 

Safe buys or guesses are Laptops with Intel cards from Lenovo, Dell, or Asus.
Different Distros may 'solve' some os these problems. Feel free to ask older members on the team's Slack about this topic

## Bash
Alot of the time, the Terminal will be used for interfacing, and so using it in a broad sense is a good start to understand it.
Check out the following link for a tutorial, with context with ROS
- https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/linux-for-robotics/

# ROS (Robot Operating System)
This is a software package that makes integrating various algorithms or sensors much easier than using a proprietary API.
It also has the advantage of working with multiple programming languages, while also abstracting away LAN networking.
ROS2 is made to address some shortcomings of ROS1(Feel Free to look this up).

## ROS 2

Check out https://docs.ros.org/en/humble/Tutorials.html and run the tutorials

Depending on if you have time, I would recommend to try the following challenges

### Challenge

Using turtlesim, get the turtle to do figure 8s, using 2 methods
1. using a timer to determine when to turn
2. using the odometry signal to determine when to switch directions

This is a quick challenge, an experienced ROS2 dev can write the two of these up in about 2 hours.
(See the workshop_ws for solution)
#### Extended challenge

do it in C++

## ROS 1

Some things are still in ROS1, however most of the same concepts still exist
http://wiki.ros.org/ROS/Tutorials
Given that ROS1 is End of Life in 2025, we are not actively supporting this one, except for edge cases.

Here is a video Tutorial if you are interested as well
- https://www.youtube.com/watch?v=wfDJAYTMTdk

# Docker 
Docker containers are used for both deployment and development. Understanding what is happening under the hood along with how to write your own makes things much easier
The following link is a tutorial on what is docker is, and how to write dockerfiles
- https://serversforhackers.com/s/docker-in-dev-v2-i

We often have multiple docker images that need to be brought up all at the same time. This is where docker compose comes into play
- https://serversforhackers.com/s/docker-in-dev-v2-ii

# C++
C++ is complicated, and so this is a last resort for most of the code written for the team. Here is a tutorial, but don't expect to use this thought the time on the team.
- https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/cpp-for-robotics/ (Requires Account)

# Recommendations

## Joel Deen
From my experience, getting started with Python, then getting your feet wet with Python is a good way to start due to its simplicity, and the fact that it is our go-to language. 
From there, get started with ROS2, and try to write various challenges. There are an assortment of ROS2 robots in Simulated environments that are available.
Then learn docker as a final step, as that should be the last thing you need to do.
