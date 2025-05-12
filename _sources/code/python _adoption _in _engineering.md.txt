# Adopting Python in engineering  
## My own personal use

I have the kind of mind that just gets drawn to coding. I find it completely fascinating. I really enjoyed using MATLAB in university and I've really enjoyed using Python since I started using it in 2020.  

It wasn't long after I started using Python that I found little ways of using it at work. Initially I just did simple calculations I could have done in a spreadsheet in a Jupyter notebook instead. Some of these things included:  

* simple pipe thrust block calculations  
* calculating the velocity needed to push air pockets downhill in a pipe using the formulas in H R Wallingford Air problems in pipes   

I also automated the production of graphs and tables tracking the rate of progress of our ICE trainees. The script reads csv reports you can get from the ICE (if you're a training scheme administrator) which tell you where all the trainees are in their training at the time the csv is produced. The script reads all the csvs (past and present) to plot progress over time.  

I moved on to create a tool for scheduling all the individual components you need for building manholes to UK water company specifications.  

I've got quite comfortable using Jupyter notebooks as my go to format for producing calculations.  

The most ambitious use I've made of Python is to develop a library for hydraulic calculations (1D steady state) which is providing the back end for an application (I haven't had so much to do with the app development, other than user testing). I was very keen to try hard to adopt good practices when developing the library so I've learnt how to:

* structure a Python library and package it using Poetry  
* test it using pytest  
* write documentation in Sphinx (a skill I used to build this website)  
* configure Sphinx so it can include md, Google doc-strings, matplotlib plots, Jupyter, REPL, the list goes on, so much configuration and so many little syntactical pitfalls  
* linting with Ruff  
* typing with MyPy (I am late getting started with that so I'm "gradually typing" i.e. slowly correcting all the slightly wrong type hints I wrote before installing it)  
* use Git and GitHub  
* use GitHub Actions to run the pytest tests, doctests, check coverage, linting and that the Sphinx docs succeed in building (thanks to my colleague Ryan Gilchrist for setting that up, it's invaluable)  

I've also had to come up with an architecture for the library. This has been a really interesting challenge and I hope the design choices I've made will continue to make sense if the library grows in the future.  

## Helping others get started  

### The set up

This is currently a very big challenge for me. It just isn't very easy guiding beginners through all the hoops to get Python set up on their system. There's so much more than just Python to worry about, you've got;  

* to set up an editor (generally VS Code)  
* to teach them how and why to create virtual environments (if using Poetry that means getting pipx first)  
* to get the necessary extensions added to VS Code  
* to help them remember how to get their environment activated when they want to use it (hard to remember if you're not doing it regularly)  

This is a lot before you get into the inevitable snags every coder hits. And this all makes it tough for people to get into it because time is valuable. You aren't getting to the good stuff while you're grappling with the set up. 

So recently I've been thinking about how to lower the barriers to entry. I have thought about it before. Probably a few years ago I tried to get help from IT to set up an internal Jupyter Hub but couldn't get the help I asked for. I'm currently thinking of looking at:  

* GitHub Codespaces  
* Marimo editable notebooks  

The Marimo option looks great for beginners, and as a replacement for Jupyter and Streamlit for more advanced users. Codespaces is probably better for coders who are looking to contribute code to projects (approved libraries and apps).  

My aims are to remove as much set up as possible and to make environments consistent so people can just get on with the interesting stuff, the engineering and to make it easier to work together.  

I would have preferred the hydraulic experts involved in the development of the hydraulic library and app to have at least experimented a little with the Python library first hand. I think part of the reason they haven't is reluctance to try, but it's also the faff I've described of getting set up. It's quite a lot of work. I'd like to set up Marimo so you can launch a notebook from any branch of the library and try out the code under development without the need for a Python environment set up locally on your machine. I imagine Codespaces could be made to do this.  

### Training  

I've run a number of Python workshops. There is a fair bit of interest but the set up issues have drastically affected how much time has been productive in the workshops. I've always lost a lot of time helping people with snags in their set up.  

Where the workshops have succeeded (I hope) is in showing how Python can be applied to engineering problems and how even with rudimentary knowledge you can do things that are extremely hard to do in Excel (I've made heavy use of Scipy's root finding, optimisation and interpolation functions).  

I am hoping to breathe new life into the workshops by getting an installation free option up and running.  

I also think it's about time to try to find really little projects for trainees to get stuck into. That's when things started to click for me.  

## Deployment  

I'm still struggling with this one. Most of what I've coded has stayed with me. I've not managed to deploy