# Overview

Let's assume that we have a piece of code that we are not familiar with. For instant this trivial function:

```python
def foobar() -> 123:
    pass
```

We would like to find path to the certain object existing in runtime. In our case we would like to find out how to programmatically access `123` in annotation of the returned value. We can guess that this information is somehow bundled to the function itself. Base on that, we can apply `digitout` to this target:

```python
import digitout
digitout(foobar)
```

`digitout` will open an interactive dialog where we need to specify what we are looking for by defining constraint expression. `digitout` will traverse through the memory and stop at the first match. Alternatively we can pipe all the paths to another tool like [fzf](https://github.com/junegunn/fzf), which will help to find the object of our choice. Let's watch how it works:

<asciinema-player autoplay=true preload=true speed=2 font-size=9px src="assets/demo.cast"></asciinema-player>



