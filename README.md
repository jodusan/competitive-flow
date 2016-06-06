# Competitive flow for CodeForces

This pair scripts allow you to faster test your CF problems by avoiding insane habit of copy-pasting tests every time you change a line of code. It is also useful for building an index of all source files from competitions.

It works by adding simple json object, enclosed in C++ comment, to source file with tests & info about the problem.

I suggest you use std::cerr for debug messages as you can leave them and they won't interfere with stdout.

## Installation

Download to your project directory, add it, and commit.

```sh
pip3 install pyperclip
git clone https://github.com/dulex123/competitive-flow
cd competitive-flow
sudo ./install.sh
```

## Usage

Edit `README.md` with the name of your project, a description, installation instructions, usage instructions, how to get support, and how people can contribute to your project.

## Support

none, nada, aucune...

## Contributing

Fork the project, create a new branch, make your changes, and open a pull request.

We use [Clear code](http://introcs.cs.princeton.edu/java/11style/) writing guidelines.
This tool can convert nicely to pdf [MarkdownToPdf](http://www.markdowntopdf.com/)
