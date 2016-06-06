# Competitive flow for CodeForces


This pair of scripts allow you to faster test your CF problems by avoiding insane habit of copy-pasting tests every time you change a line of code. It is also useful for building an index of all source files from competitions.

It works by adding simple json object, enclosed in C++ comment, to source file with tests & info about the problem.

I suggest you use std::cerr for debug messages.

![Competitive flow](https://media.giphy.com/media/xT8qBhwuiiXczRZBAI/giphy.gif)

Or you can watch slower 30sec [youtube video](https://youtu.be/vFjqoGfHRBk)

## Ubuntu Installation

```sh
pip install pyperclip
git clone https://github.com/dulex123/competitive-flow && cd competitive-flow
sudo ./install.sh
```
Now you just need to assign shortcut for cf-paste command.  
For gnome users this is in gnome-control-center -> keyboard -> Shortcuts -> Custom Shortcuts. (Super + V)

## Windows Installation

- If you are not using codeblocks default installation dir for your compiler you need to change third line in install.bat to compiler bin folder that includes g++.exe.
- You need to run install.bat with "Run as Admin" privileges.  

```sh
pip install pyperclip
git clone https://github.com/dulex123/competitive-flow
cd competitive-flow
install.bat
```
To make a shortcut for cf-paste  
1. Right click C:\Program Files\CompetitiveFlow\cf-paste.py and create shortcut  
2. Right click shortcut file and go to properties select hidden  
3. On Shortcut tab find Shortcut key: entry and add some shortcut (Ctrl+Alt+V)  


## Usage in 3 easy steps

1. Copy test samples from codeforces problem page including first "Input" string  
2. Press shortcut to modify clipboard content with cf-paste  
3. Paste into .cpp source file  

Thats it! 

From now on you can test your program with 

```sh
cf-tool CF-345A.cpp 
```
