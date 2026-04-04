# Git tips

I've not really got to grips with the behemoth of version control systems. So this page
is kind of my survival tips for remembering how to do things I find useful but easily
forget. 

## How to make git prefer changes made on your non-working branch  

Sometimes I end up in the situation where I want to update my current working branch 
with changes (normally on `origin/main`) without having to go through the pain of 
resolving conflicts (because I know I want to accept everything from main).  

The trick to this is 

```bash
$ # Make sure everything is up to date first
$ git fetch
$ git pull
$ # Merge all changes from main
$ git pull -s recursive -X theirs origin main
```

The `-s` flag allows you to choose a merge strategy, in this case `recursive`.  

Within `recursive` the `-X` flag allows you to choose options, in this case `theirs` 
prefers changes from the non-working branch.  

This did the trick for me. One gotcha is that I'm used to the command:

```bash
$ git merge origin/main
```

So it caught me out that I needed a space instead of a forward slash.  

Thank you to [bric3](https://stackoverflow.com/a/21777677/16472589) for this solution.  
[Official docs](https://git-scm.com/docs/git-pull) (so hard to read)

## Conflict between VS Code's "Merge Editor" and GitBash  

I got so confused as to why VS Code kept crashing when I tried to fix conflicts. The 
issue is that I like to work with GitBash in Windows Terminal. Unfortunately it seems 
these two things conflict with each other. So the easy fix is:  

> Close the GitBash window in Windows Terminal before trying to resolve conflicts in 
  VS Code  

Easy.