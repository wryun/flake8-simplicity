**Lint your Python like it was 1999!**

Do you ever miss the days when your coworker couldn't
convert 10 straightforward lines of Python into
a mess of decorators and multiline dictionary
comprehensions?

Would you like it if no-one could make annoying comments
on your PR about how you could make it 'nicer' by
using with, walrus operators, and yield?

Could you pass on deciding to rewrite your
entire application to use async?

Think that maybe there are 27 ways to do it in today's
Python, and that that's pretty damn annoying?

*Then install flake8-simplicity today.*


# Motivation

I was whinging aimlessly about the latest changes to Python
to a co-worker, as you do, and claimed that sometimes I wish
I could do:

```
from __past__ import simplicity
```

But hacking the Python interpreter seemed non-trivial, there's no
chance that the PEP would get up, and also no-one would use it.
A linter, on the other hand...


# Usage

This is a flake8 plugin. So...

```
pip install flake8-simplicity

flake8 myfile.py  # or however you like to lint
```

Errors from flake8 simplicity are prefixed with SPL, and are
perhaps not the most informative. A PR to create a humourous
message for each infelicity would be gladly accepted.


# PS

Yes, I'm aware of the irony of using `yield` statements
in this code.
