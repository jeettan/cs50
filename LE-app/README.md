# Health App: LE-DATA

Hello world

#### Video Demo:
https://www.youtube.com/watch?v=8Z4q1akw3WQ

#### Description:
This is a health app to track and facilitate the healing process for a disease called Lymphedema.

#### The PROBLEM:

Lymphedema is a a chronic disease that requires daily treatment.

Treatment is done by using a series of wrapping material and wrapping the affected body, with a 15 minute interval + 5 minute break for about 10 intervals/day, for management.

A standard at-home course would be opening up a YouTube video with a timer, pressing play, wrapping, going back to the YouTube video, setting up a 5 minute break, etc.

Another typical way of recording the time would be using your phone and doing the timer manually.

However, this process takes thought away from the actual treatment itself.

#### The SOLUTION:

This app is split into three sections:

#### Section 1: Timer

I created the timer section to resolve the problem of having to think through setting up timer. It's as simple as pressing a button and the information gets recorded automatically. Information that gets recorded is the number of wraps that get completed after each cycle. Information gets stored in a .json file and is read upon entry of application.

Timer is created in the form of a tkinter widget instead of a webpage to keep things manageable.

#### Section 2: Data collection

I added data collection section for habit tracking and figuring out how many times of a wrapping cycle I have done / day for logging. The data collection takes the data that is inputted based on the results (before/after) of the course and exports it to a CSV file for reference.

You have the option of saving to a JSON file and which gets loaded upon entry.

#### Section 3: Information

I added an information section which is a button that links to relevant content.

#### Conclusion:

These three sections combined helps make the treatment process smoother and lessens the strain on the brain in terms of focus.

Remember, treatment is not simply just going through the motions, it has a degree of discomfort and pain.

So, lessening the strain such as having to think, about "where is my timer" or "how many times I've wrapped," makes the process much more easier.

#### Usage:

1 - cd to directory 2 - python lymphieapp.py

#### Libraries used:

-Tkinter
-Subprocess to open separate python programs
-Pygame
-Atexit
-Customtkinter

#### Possible Improvements:

1. First is to improve the UI and make it look better.

2. Second is to be able to export to a CSV that tracks the progress over weeks/months instead of one day at a time. Through this, I'll be able to plot the data on a graph for reference.

3. Improving content base. In general volume of content is always helpful, in an organized way so that you have information at your disposal to aid you in the treatment process.

#### Lessons learnt:

I learnt many lessons. First is to break things down into manageable chunks. Second is to understand the problem you are solving and then figure out what's the best solution for that problem. For example in my case, I wanted to create a widget so I figured that using python is the best course of action compared to javascript. Next is to keep on persisting and don't be afraid to experiment.
