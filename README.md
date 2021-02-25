# Donder's Experiment of Mental Chronemtry 

Donder's reaction time experiment tests your reaction time when presented with a stimulus. You will observe that when you are presented with a choice, your reaction time is slower, as seen in a sample experiment result below.

This application boots up a GUI to test your reaction time in two parts. You are first tested by acknolwedging a white circle as soon as it appears on your screen by pressing the space bar. After a user-specified number of iterations, it switches to displaying a white circle on either the left or right side of the screen. You must press the left arrow key as soon as it appears on the left side of the screen and the right arrow key when the circle appears on the right side.

When the experiment concludes, the results are generated to a text file called ```results.txt``` in the same directory as the running Python file. A sample of the output file with experiment iterations set to 3 is below. 

```
CENTER LIGHT
256.82
455.869
288.589
AVERAGE: 333.75933333333336

===============================

LEFT OR RIGHT LIGHT
588.428
383.266
363.666
AVERAGE: 445.11999999999995

```

To run the application, first make sure you have Tkinter for your version of Python. Then run ```python experiment.py``` from the command line.
