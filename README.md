# Mars Rover Problem
ThoughtWorks MarsRover Problem

## Problem

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

##### Input:
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.
Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.

##### Output:
The output for each rover should be its final co-ordinates and heading.


**Test Input:**

5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

**Expected Output:**

1 3 N

5 1 E

## Project Structure 
Lorem
 
## Design

The input is first parsed completely and 'translated' to corresponding plateau, mars rover and command objects. Per default, the input (and output) is read (written) to txt files that can be determined as command line parameters.
After successful parsing, the commands are executed sequentially and output written to the output file.

The Python 'logging' module was used to give more information on the program execution and possible errors. With it's different logging levels (ERROR, INFO, DEBUG) it facilitates code maintaining and debugging for developers.

#### Assumptions
* Rover cannot move out of grid
* There can be more than one rover on a given grid coordinate
* 0-coordinates are still part of the plateau ((0,0) is a valid coordinate)


#### Design Choices
The Command Pattern was used to encapsulate different mars rover movement commands. This way, it is easier to extend the program, for example by supporting more complex rover movements.

* Separation Model and Control
* Classes for modularisation
* direction abstraction to allow more complex extensions (e.g. North-West)

#### Used Style
[PEP 8 Style](https://www.python.org/dev/peps/pep-0008/)


## Dependencies
* python3.7+

## Install
Clone or download project (and unzip if necessary).

Navigate into project: ```cd marsrover```

Install program: ```python3 setup.py install```

## Run 
Run Program: ```marsrover -i sample_input.txt``` 
(reads from input file and writes into default output file)

#### Optional Arguments
Specify output file: ```marsrover -i sample_input.txt -o sample_output.txt``` 

Run in verbose mode: ```marsrover -i sample_input.txt -v```


