# WOGO brief  

Work out, geek out (WOGO) is an idea for a personal project to write a command line tool so I can track my progress with upper body exercise. I'm planning to write it in Rust, compile it with Linux as a target and I can't see why it shouldn't be possible to run it from the command line on my iPhone using iSh. 

## User interface  

The user interface will be intentionally minimal. Initially I'm just going to aim for the below;  

```bash
$ wogo # start the tool  

Hi Sam
Time to WOGO (Work out, geek out)  

Please select from the following:  

1 Record set of pull ups  
2 Record set of chin ups  
3 Record set of hammer grip pull ups  
q to quit and save  

> one  

Input error; Please enter a number according to the selection you want or q to quit.  

> 1  

How many reps of pull ups did you do? [integer]  

> 2  

Did you continue until failure? [y/n]  

> y  

You've recorded that you did 2 pull-ups and continued until failure. Enter [y] to confirm or [n] to discard.  

> y  

Please select from the following:  

1 Record set of pull ups  
2 Record set of chin ups  
3 Record set of hammer grip pull ups  
q to quit  

> q

```

The user interaction above would create an entry like this in the dataframe.  

| timestamp | pullups | chinups | hammers | to_failure |
| --- | --- | --- | --- | --- |
| 2025/05/26 19:19 | 2 | nan | nan | `true` |  

The timestamp would be added automatically from the time the entry was made.

For a session involving multiple sets you can just continue to loop through the questions until you're finished then quit.  

Any necessary corrections will initially need to be performed outside the app (e.g. in a Python REPL).  

## Data storage  

It would be perfectly possible to store the data in a simple csv but I'd like to learn a little bit about Arrow and Polars so it'll be a project requirement that the tool will read and write to a feather file.  

## Configuration  

The first time the app is run it'll require a configuration as below;

```bash
$ wogo

Welcome to WOGO (work out, geek out).

To get started please give your name

> Sam

Please give a filepath to where you want to store your data 

> home\some\path

```

This will write to a file called wogo.toml which will store the user's name and location of their data so the user won't need to specify this each time.  

## Visualisation  

I plan to use Python with Sphinx or Marimo to create visualisations using matplotlib. This will probably be in the form of bar graphs and maybe some table created with great tables.  

## Additional features  

Some things it might be nice to add.

- correcting entry errors  
- add new type of workout  
- display recent activity  

