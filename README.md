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

## Bigger Numbers Branch
This branch just uses much larger max random numbers than the base branch, which sticks to 1-120. Both are going to be refactored to have fewer integer literals.