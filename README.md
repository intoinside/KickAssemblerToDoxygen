![GitHub](https://img.shields.io/github/license/intoinside/KickAssemblerToDoxygen?style=flat) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/intoinside/KickAssemblerToDoxygen/python-app.yml?style=flat) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/intoinside/KickAssemblerToDoxygen?style=flat) ![Coverage](./coverage.svg)

# KickAssemblerToDoxygen

## What is this
This Python script provides a simple conversion from 
KickAssembler source code into C-like format. This new syntax
is readable from [Doxygen](https://www.doxygen.nl/index.html).

Converted files are not meant to contain valid source code.

This script is not perfect and suits well for most of the 
KickAssembler source code. Feel free to improve it.

## How it works

Usage: python KickAssemblerToDoxygen.py &lt;folder-name&gt;

Example: python KickAssemblerToDoxygen.py .\\lib

Output file will be automatically created in "output" folder
inside folder passed by argument.

Remeber to use slash or backslash correctly.

It works with Python 3.10 and (hopefully) above.

## Statements supported

This script removes:
* .assert
* .asserterror
* .filenamespace
* .importonce
* .import

After removing all these stuff, it fixes struct declaration.

Next step is to remove initial dot from keywords and then add a semicolon at the end of every label and const declaration.

This sequence is repeated for every file specificated as argument and edited file are saved in output folder.
