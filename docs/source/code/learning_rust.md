# Learning Rust as a Pythonista

## Background, why Rust?

I'm picking my way very slowly into learning Rust.  The thing that got me really thinking about it is at work I'm developing a Python library and it's just not as fast as I'd like, so even though a re-write isn't necessary just yet it got me interested in possible ways of speeding things up. I've been impressed at just how much faster ruff is than flake8. I knew the principal reason for this is that ruff is written in Rust whereas flake8 is written in Python. 

I also looked into Cython, it looks like a very tidy solution in a lot of ways but it can get pretty complicated and like C and C++ it isn't memory safe. I'm not sure just how big a deal that is for numerical computing but colleagues at work didn't like the idea of doing something new in a non-memory safe language (partly in light of the Whitehouse report on memory safety).

I was aware from listening to various podcasts how learning C or C++ would be a big undertaking and besides, my company would probably be even more nervous about me using one of those languages than Cython.

I also looked into Julia but was put off that by how it seems to me that it wouldn't play nicely with the Python I've already written and Julia didn't look as interoperable in general as Python.

Some colleagues mentioned Rust as a possibility. It's on the Whitehouse list of memory safe languages. It was somewhat on my radar already so I decided to investigate a bit more.

There is a part of me that was interested in  learning a lower level language for its own sake just to improve my understanding. 

I've started the Rust book, the Rustlings course and Rust by example. I've also listened to the whole "New Rustacean" podcast. A lot of the podcast went over my head but I'm sure I'm understanding what I'm reading better because of listening to it.

## First impressions

### The tools 

I installed `rustup` on my personal laptop and I could hardly be more impressed by the package you get out of the box. 

At work I've been spending a lot of time trying to learn best practices when it comes to coding and finding and learning the right tools for the job has taken a fair bit of time in Python. It's a process I've found interesting and I like my Python tools but I was really impressed to see how `rustup` has an equivalent to most of the Python tools I use.

|Description|Python|Rust|
|---|---|---|
|Package/dependency manager|Poetry|Cargo|
|Documentation|Sphinx|rustdoc|
|Testing|pytest|Cargo|
|Linting|ruff|Clippy|
|Formatter|ruff|rustfmt|

The Rust language server in VS Code is also very handy, very similar experience to having the ruff extension in Python. 

I'm still yet to write even the most basic program of my own in Rust. I think something I'm likely to find the biggest  difference is how in Python I often experiment and iterate in Jupyter or a ptpython (normally ptipython) REPL. Rust, being a compiled language, doesn't have an equivalent to that really rapid feedback environment. So I'm guessing that writing tests and running `cargo test` would take the place of what I often do in Jupyter or ptpython. This would be slower but in another sense it might be better in that I know I don't write all the tests I do in Jupyter or ptpython into pytest, I just run them and delete them. 

There is the Rust playground which I've yet to experiment with much but that could allow for some more rapid experimentation. 

### Teaching materials

I've also been very impressed with the official learning materials. Something I wasn't expecting was to find that the code samples in the Rust book and Rust by example websites are interactive. Yes, you can edit and run them in the browser. This is great for learning. Jupyter is developing Thebe to do this sort of interactivity in Sphinx but the websites I've tried it on always seem to crash. The interactive code in the Rust websites just works.

## Language differences

I think it's fair to say that Rust is more verbose than Python. You need to write more code to do the same thing. However, even at this early stage I can see some very clear benefits to the way Rust makes you do certain things (in case you don't know, the Rust compiler will not compile your code if it detects a whole host of errors or bad practices). 

### function returns

Rust always returns an enum from a function which is in one of two states `Ok` if everything worked or `Err` if there was an error. When handling the return from a function you have to explicitly deal with what happens if that function throws an error. 

In Python I've either dealt with this by having the function raise an exception which forces you to write `try` `except` blocks (or risk run time errors), or return named tuples `(result, valid(bool))` where you run the risk of forgetting to check your result is valid. 

Rust's enum return idea makes a lot of sense. 

### forcing you to consider all the possibilities

The way Rust forces you to consider what happens goes further than the example above. Unless I'm misunderstanding it it looks to me like Rust won't let you miss a logical possibility. 

In Python it's very easy to miss a potential state with a set of `if` `elif` statements. Rust's pattern matching does seem to make it easier to get complicated logical checks correct. 

### immutability by default

Something that confused me for a while learning Python was how people talked about some objects being mutable and others being immutable. Tuples and strings are immutable but you can do the following

```python
>>> a = (1, 2)
>>> a = "new value"
>>> a
"new value"
```
That doesn't look very immutable. The reason is that even though the tuple and string objects are immutable, the variable `a` is mutable. So you can't change the "2" in `(1, 2)` to any other value, but you can change `a`. I don't think I'm alone in initially finding that confusing. 

In Rust however, the variables can be (and by default are) immutable. So you can't just go and re-assign their value like you can in Python. This is more like what I expected immutability to be like. Rust does allow you to shadow previously defined variables if they are immutable if you use the `let` keyword again but the shadowing only applies in the current scope. 

## final thoughts

I'm enjoying my first steps learning the language. It's very different to Python.  It's compiled, not interpreted; statically typed, not dynamic; it's not object oriented. It has more complicated enums, it has structs, traits, borrow checking, lifetimes. So many things that are very different. But as proven by ruff and polars and others, Rust works really well with Python. It also works very happily on its own or interacting with other languages. It's very very fast. It stops you making the scary mistakes that are possible in C, C++ and FORTRAN. It has fantastic tooling out of the box. I'm pretty sold on it. 