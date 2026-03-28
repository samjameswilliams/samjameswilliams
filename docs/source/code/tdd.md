# Why I'm sold on test driven development  

## My background  

I'm a chartered civil engineer working in the UK water industry. I did a little MATLAB coding in university but didn't touch code between 2007 and 2020 when I started learning Python.  

As a professional  civil engineer I learnt the importance of quality control and checking. It's important to remember that everyone makes mistakes. In civil engineering mistakes in drawings and calculations can be dangerous, it could cost lives. So no matter how good the engineer is who did a piece of work, it always gets checked. The higher the consequences of failure or complexity of the design, the more rigorous the check should be. 

When checking drawings and calculations it is good practice to record what you've checked as you go and hold on to that record. Typically for me drawings have been checked on a pdf print and calculations in an Excel spreadsheet. The checking is a very manual process. 

Whilst that may sound inefficient, for bespoke work it isn't necessarily. In fact, especially these days, there's much to be said for the human element involved in this style of quality control. Where it becomes more problematic is when it is applied to standardised calculations. If a standard calculation spreadsheet has been through checking and in use a bug is discovered, or a new feature is required, the manual check of the spreadsheet needs to be repeated. Will you remember to check all the things from the first round? Were the checks all recorded? There's a high risk of unintended consequences from the changes.  

## Getting into Python

When I started work developing an internal Python library for hydraulic calculations I was keen to learn how to do quality control in a code context. I loved the idea of having automated tests that were re-runnable as you went. It really helps overcome the issue of unintended consequences of changes. 

Till then I'd used Python in Jupyter notebooks and had taken a very similar approach to checking as I always had in Excel, doing manual sense checks as I went. 

To begin with my approach to writing a new feature went something like:  

1. Write and experiment with the feature in Jupyter interactively.  
2. When it worked as I wanted, copy it into the library.  
3. Write tests to ensure it keeps working as intended.  

This was a step up over Excel but I still had the following issues:  

* sometimes things that had worked when I tested them interactively earlier were broken by the time I wrote the tests later  
* although my code might do what I wanted, the API was sometimes very ugly to work with  
* it was often quite tricky to write clean tests to test my code  
* I must have done hundreds of interactive throw away tests that never made it into the test code    
* the tests weren't getting full coverage of the code (some lines of code weren't activated in any test)  

## The lightbulb moment  

I'd heard the term "test driven development" in various podcasts but almost invariably it was someone saying something like they didn't have the patience for it. I didn't really know what it was but when I saw an invite going round for my colleague Ian Cornwell speaking on test driven development I decided to dial in. As I watched I saw how the way he applied test driven development addressed all the issues I outlined above. I thought, I need to start doing things this way. 

## So what is test driven development?  

Before you write any code at all you first write a specification of what the code should do. The specification doesn't need to be a formal report. Often for me it's a checklist which I keep in a GitHub Issue. Ideally you should agree on this specification with a domain expert (someone who understands the problem you're trying to solve with the code, not necessarily a coder), even if you are a domain expert yourself it's good to bounce your concept off someone else.  

Ideally the specification should include examples of expected output from a given set of inputs. This should include as many types of scenarios as you can think of. It is also good to identify clearly what is valid and invalid input and output.  

It can be tempting to dive straight into coding but thinking things through like this pays dividends in the end. I was already fairly close to doing this part already. In my non coding calculations and drawings I always come up with an outline or sketch of what I want to do and agree that with people before diving into the detail. It saves a lot of rework.  

Having done this you choose a part of the specification you can write as a test in code. Then you write that test and run it **before** writing the code to do what your testing. Yes, it sounds odd but there's a few good reasons. 

Firstly, the test ought to fail. If it doesn't then there must be something wrong with the test. It's as easy to make mistakes when writing test code as any other code. Also you get to see an error message, this is also often informative. Has it failed for the reason you would expect?  

Additionally, it makes you think about the API before the implementation. You'll probably think as you're writing the test "how would I like to call this function or instantiate this class and how do I want the results"? You'll probably write something that is nice to work with and so you'll end up with something that's nice to work with. 

You also won't want to write huge tests with complicated set ups so it makes you write code that is easy to test. This type of code tends to be highly modular and reusable.  

Then you write the least amount of code you can to make the test pass, even if you know you won't keep it because you know something will come later that will force you to do something different. Why do this? Because it avoids non-functional code getting in and should ensure full test coverage. If there's non-functional code in the code base there's a reasonable chance the code isn't doing something you think it should. If you haven't got full coverage there's a higher chance you'll get unexpected behaviours from the code in use than if you do.  

Then you refactor the code to make it cleaner and rerun the tests to see if it still works. You do this until you're happy. Then you write another test and go through the process again. You keep repeating until everything in the specification is covered. 

## When I don't use it  

I'm just getting into simple GUI development using Marimo. I don't see as much value testing the front end as the back end. But if I were doing something more complicated I'd think about a front end testing framework like Playright. 

For simple scripts or notebooks for calculations I generally don't do test driven development. Ian however uses it even for the Advent of Code challenges because he's so used to it. So maybe I'll end up using it for more one off code too as I get quicker with it. It does give confidence in what you're writing.

## What if ...

**What if I've already got a really nice code architecture in mind and following test driven development leads to something else?**  

This was a question I put to Ian at the workshop. What he said was that he doesn't go through the spec sequentially but looks carefully at what the next step should be. He sometimes has an architecture in mind at the outset but he remains open to arriving at something simpler if it'll do the job. The test driven approach is a good way to put your idea to the test. 

**What if you realise something in the specification isn't right part way through?**

This is quite likely. It's hard to spot all problems in advance. If that happens you might need to revisit some tests, but it's a similar process doing that to writing new ones. Code coverage tools can help to identify if removing a badly designed test has left untested code in place. 

**What if I need to work on ideas in an interactive environment?**

I still experiment and check my understanding of how things work in an interactive environment. But I do it a lot less. I tend to just check how individual functions or methods behave or how to access attributes rather than develop my new feature in an interactive environment. I've also switched from using Jupyter notebooks to using ptpython in ptipython mode. It makes it feel more throwaway if it's in a REPL rather than saved in a file somewhere, and that's a good thing. It's important to get away from tinkering and writing too much by trial and  error if you're going to embrace test driven development.

## Is this still relevant in the age of AI?  

I'd say yes. It's still important to be able to prove the code works. It's still desirable to get the job done with the smallest, simplest code base that does the job. It's still desirable to keep code modular and have tests tightly linked to your specification. AI can be used to assist in the test driven workflow. It's probably getting rarer to find people who don't use AI somehow. But one way AI works against the test driven philosophy is it tends to write incredibly verbose code. It will write code more quickly than you can review it so you need to keep it on a tight lease and be ready to just use `git reset --hard` ruthlessly if it generates reams of code rather than waste time debugging it all. 

## Closing thoughts

I know there's other ways to ensure you get a robust, clean code base. But for me after trying to figure it out on my own this approach made a huge difference. I spend far less time debugging, the code coverage on new stuff I write is 100%. I'm sure there's fewer bugs in the end result. I feel more confident refactoring and in what I've done overall. It has a nice methodical feel to it, it's great putting tick marks on things in the spec as you go through knowing those  ticks all represent at least one test. It makes it easier to gauge how far along you are. As I say in the title, I'm sold on it. 