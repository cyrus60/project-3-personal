# Project 03
**CS-1160 Wright State University | Dan Grahn**

> Reminder: In order to maintain academic integrity, you are required to cite any assistance you received outside of course materials. See [Citing Sources](citing.md) for examples.

## Introduction
The purpose of this project is to provide you with more practice using conditional statements, loops, and functions. Your task is to write an interactive terminal that allows a user to display simple shapes using text symbols.

## Requirements
The application must be written in `project_02.py`. Make sure the file contains a comment at the top of the file with the following information.

1. Your name
2. The date you last updated the application.
3. The application name
4. A short description of the application

When the application is run, it should display a header message of your choice. The header message should identify the application and inform the user of how to request help. Next, the application should prompt the user for input. Whenever the user is prompted for input, the terminal line should start with three greater-than symbols (i.e. `>>>`) just like the Python terminal. For example:

```
$ python project_02.py
Sarah Saturday's Shape Printer 1.0.0 (Oct 15 2021)
Type "help" for more information
>>> 
```

The terminal should accept 5 commands. These commands should be case-insensitive. Provide a mechanism to allow a user to recover from an error. Once a valid command is detected, check the validity of the parameters. You may assume that parameters which expect a number are numbers. However, the number may not be within the accepted limitations.

## Program design
To solve this program, you need to decompose the problem into manageable pieces. Fortunately, the program naturally breaks into functions based on different commands. Design your solution so that your main program calls functions to complete the different commands. For example, there should be functions to respond to each command and one or more functions to get valid commands.

## Commands
### `box`
The `box` command prints a rectangle.

| Parameter  | Limitations           |
|------------|-----------------------|
| Print Type | "filled" or "outline" |
| # of Rows  | 0 < rows              |
| # of Cols  | 0 < cols < 50         |

#### Examples
```
>>> box filled 4 6
******
******
******
******
>>> box outline 4 6
******
*    *
*    *
******
```


### `right`
The `right` command prints a right-triangle.

| Parameter      | Limitations           |
|----------------|-----------------------|
| Print Type     | "filled" or "outline" |
| Length of Base | 0 < base < 50         |

#### Examples
```
>>> right filled 5
*
**
***
****
*****
>>> right outline 5
*
**
* *
*  *
*****
```


### `iso`
The `iso` command prints an isosceles triangle.

| Parameter      | Limitations                  |
|----------------|------------------------------|
| Print Type     | "filled" or "outline"        |
| Length of Base | 0 < base < 50, base % 2 == 1 |

#### Examples
```
>>> iso filled 7
   *
  ***
 *****
*******
>>> iso outline 7
   *
  * *
 *   *
*******
```


### `quit`
The `quit` command exits the terminal. It does not take any parameters.


### `help`
The `help` command prints an informative help message of your design. 

| Parameter  | Limitations                   |
|------------|-------------------------------|
| Command    | Valid command name, optional. |

#### Example
```
>>> help
Welcome to Sarah Saturday's Shape Printer.

The following shapes are available.

1. Box (command: box)
2. Right triangle (command: right)
3. Isosceles triangle (command: iso)
4. Diamond (command: diamond)
5. Quit (command: quit)

>>> help box
The "box" command prints a rectangle.

Parameters:
    type: Print type; "filled" or "output"
    rows: Number of rows, integer greater than 0
    cols: Number of cols, integer between 0 and 50
```

## Grading
Grading will not be done automatically on push like the labs. Instead, it will be performed after final submission. Your application will be tested against a range of inputs which are designed to make it fail. It will be graded against the following criteria.

Correct output (55 pts)
Correct input validation (35 pts)
Clarity of code and comments (25 pts)

Take time to consider the different "edge cases" that could be given to your application.
