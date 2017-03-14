# piday2017
A fun experiment for Pi Day.

## What does it do?
This is a Python implementation of the method used in the video that StandUpMaths put on YouTube today, which you can watch [here](https://www.youtube.com/watch?v=RZBhSi_PwHU).

If you don't want to watch that, then I'll put it simply: This program attempts to approximate pi (yes, _the_ pi) using the probability that two random numbers are coprime.

Did that not make sense? Well, go watch the video. They did a great job explaining how this program works.

## How do I use it.
`python3 randompi.py`

Just type that in. Yeah, I'm using Python 3. No, I don't intend to backportit to Python 2. It's time to upgrade, people.

The program is quick and dirty, but it gets the job done. It will run until either it goes through every possible positive integer on your system (`sys.maxsize`), or until you hit `Ctrl+C`.

## Componentized Branch
This branch will likely be merged with the master, as it is superior in every way to the original design. For now, though, I'll just explain how it works here instead of changing the rest of the README. Functionally, this paramaterizes everything in the program, and makes it so that it can be imported by another python program. That gives me the chance to run lots of tests and see which method (expressed in a comment [here](https://www.reddit.com/r/math/comments/5z5sxx/generating_%CF%80_from_1000_random_numbers_matt_parker/dew3yxz/). Thanks, [/u/Tomus](https://www.reddit.com/user/Tomus)) will produce a more accurate approximation of pi.

Yay!

In order to run these tests, just type:

`python runtests.py`

Be warned, it's probably going to take a while. I have yet to actually finish a full run, and I'm not timing anything. Good luck to you.