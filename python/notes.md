#### notes

-   design, build, and test large programs

    -   design
        -   construct large programs out of pieces that **interact in a small number of ways**
    -   **code is data**
        -   source code is just text
        -   a program in memeory is just a data structure
    -   making sense <- comprehension + abstraction

-   Python

    -   python's object system can be understood in terms of **dict that contain references to** properties, functions, and other dict.

    -   an object is a dict; a method is a function that takes an object of the right kind (self in python)

        ```python3
        def square_new(name, side):
            return {
                "name": name,
                "side": side,
                "perimeter": square_perimeter,
                "area": square_are
            }
        ```

        -   obj.meth(arg) -> obj["meth"](obj, arg)

    -   aliases behave like pointers in some respects

-   tools
    -   venv
        > python3 -m venv sdxpyenv
        > source sdxpyenv/bin/activate

#### reference

-   [Software Design by Example with python](https://third-bit.com/sdxpy/)
