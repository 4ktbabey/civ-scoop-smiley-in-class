# Class Activity: Smiley

This class activity will feed into Assessment Task 3.
You will find it challenging to complete Assessment Task 3 without this activity.
# The Setup
1. You will clone the repository at [civ-scoop-smiley](https://github.com/NM-TAFE/civ-scoop-smiley-in-class)
2. Read the `README.md`, and run your code from `main.py`.
3. 🙂

# The Exercise

Here, you will make some modifications to the provided code.

> [!Reference]
> If you need to step through your code and investigate what is happening, remember that you can use breakpoints:
> ```python
> breakpoint()
> ```
> `n`: Step next
> `s`: Step into
> `r`: Step out of (return)
> `c`: Continue (until next breakpoint)
> `q`: Quit
> And, just like in your REPL, you can name any variable to see its value.

### 1
We would like all of our Smileys to be able to blink.
1.1: Using `happy.py` as an example, edit `sad.py` so that it can also blink.
1.2: Rewrite your `main.py`'s main function, so that both smileys are shown.
### 2
We would like our Smileys to be various colours
2.1: What class defines the colours?
2.2: Name all colours
2.3: Add `BLUE` to the class from 1.1
### 3
3.1: Modify Smiley's constructor, so that it can accept a `complexion` parameter.  This should default to `YELLOW`
3.2: Set a private instance variable, `self.__complexion` to the complexion parameter.
3.2: Instead of setting `Y` to `self.YELLOW`, now set `Y` to `self.__complexion`
3.3: Refactor: everywhere that currently uses `self.YELLOW`, `Smiley` or elsewhere, should now refer to `self.__complexion`
### 4
After all that: let's make our Sad smiley blue.
4.1: Modify the call to `super().__init__()`, so that it can take the new `self.BLUE` parameter.
4.2: Check that your `Sad` smiley is now blue, and your `Happy` smiley stayed yellow.
### 5
Make your own Smiley:
5.1: Using `Sad` and `Happy` as templates, now define your own `Angry` smiley.  Please make sure that this smiley is `RED` in `complexion`.
Try using some grid paper and this function to draw something that you find fun:

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     |     |     |     |     |
| 1   |     |     |     |     |     |     |     |     |
| 2   |     |     |     |     |     |     |     |     |
| 3   |     |     |     |     |     |     |     |     |
| 4   |     |     |     |     |     |     |     |     |
| 5   |     |     |     |     |     |     |     |     |
| 6   |     |     |     |     |     |     |     |     |
| 7   |     |     |     |     |     |     |     |     |
```python
"""
  This function takes an x,y coordinate and returns a single number representing that position in a 8x8, zero-indexed grid.
  Necessary because the SenseHat represents the 64-LED matrix as a "one dimensional" list of RGB colours.
"""
def convert_to_1d(x,y):
	return 8 * y + x
```


---

Well done!

## Coming soon:
Here is an example of a version of this repository which contains all the modifications that we've done today, so that you can check your work:

<!-- TODO: Add link to completed branch -->