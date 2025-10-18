# pyansistring
![pyansistring Banner](./images/banner.png)

## About The Project

[***pyansistring***](https://github.com/l1asis/pyansistring) is a library for **string color styling** using **ANSI escape sequences**. The base class inherits from Python's `str`. You can split, join, or slice the string while **preserving the styling**.

### Features

* Preservation of the str methods.
* Support for 4-, 8-, and 24-bit (True Color) color modes.
* Per-word coloring.
* Left, right, and center alignment without problems caused by string length.
* Support for multiple SGR (Select Graphic Rendition) parameters.
* Support for both the traditional ";" and the modern ":" SGR parameter separators.
* Automated coloring functionality, e.g., rainbow text.

For a more comprehensive list of what's been done so far, see the [TODO](./TODO.md) section.

Inspired by [***rich***](https://github.com/Textualize/rich) and [***colorama***](https://github.com/tartley/colorama) Python libraries.

## Getting Started

### Prerequisites

* Python 3.10 or higher
    * Linux: https://docs.python.org/3/using/unix.html
    * Windows: https://docs.python.org/3/using/windows.html
    * macOS: https://docs.python.org/3/using/mac.html
* Git (for local installation)
    * Linux: https://git-scm.com/downloads/linux
    * Windows: https://git-scm.com/downloads/win
    * macOS: https://git-scm.com/downloads/mac

### Installation

You can install the package **via pip**:
```sh
pip install pyansistring # or pip3 install pyansistring
```

Or locally **via git**:
1. Clone the repository
    ```sh
    git clone https://github.com/l1asis/pyansistring
    ```
2. Navigate to the cloned directory
    ```sh
    cd pyansistring
    ```
3. Change git remote url to avoid accidental pushes to base project
    ```sh
    git remote set-url origin github_username/repo_name
    # Verify the changes
    git remote -v
    ```
4. (Optional) Create and activate a virtual environment
    ```sh
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On Unix or MacOS
    source venv/bin/activate
    ``` 
5. Install the package
    ```sh
    pip install .
    ```

<p style="text-align: right;">(<a href="#pyansistring">back to top</a>)</p>

## Usage

```python
from pyansistring import ANSIString
from pyansistring.constants import SGR, Foreground, Background

# Does what it should: prints all text in bold, with magenta foreground and white background.
print(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA).bg_4b(Background.WHITE).fm(SGR.BOLD))

# But you can do the same on a specific slice:
print(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA, (0, 4)).bg_4b(Background.WHITE, (2, 4)).fm(SGR.BOLD, (4, 6)))

# Or if you want to apply styles to a specific word
print(ANSIString("Hello, World!").fg_4b_w(Foreground.MAGENTA, "Hello", "World").bg_4b_w(Background.WHITE, "World").fm_w(SGR.BOLD, ","))

# You may find predefined colors boring, let's do it with RGB:
print(ANSIString("Hello, World!").fg_24b(255, 0, 255).bg_24b(255, 255, 255))

# And of course you can do the same tricks with words:
print(ANSIString("Hello, World!").fg_24b_w(255, 0, 255, "Hello").bg_24b_w(255, 255, 255, "World"))

# By the way...
print(len(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA)) == len("Hello, World!"))
# -> True

# Why? Because I wanted it to behave this way. But at the same time:
print(len(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA).styled) == len("Hello, World!"))
# -> False
print(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA).actual_length == len("Hello, World!"))
# -> False

# If you need the original string:
print(ANSIString("Hello, World!").fg_4b(Foreground.MAGENTA).plain)
```

<p style="text-align: right;">(<a href="#pyansistring">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**P.S.** I would love to see your arts made with ***pyansistring*** in the `arts.py` file, with proper attribution, of course!

<p style="text-align: right;">(<a href="#pyansistring">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p style="text-align: right;">(<a href="#pyansistring">back to top</a>)</p>

## Acknowledgements
* [Othneil Drew's Best README Template](https://github.com/othneildrew/Best-README-Template)

<p style="text-align: right;">(<a href="#pyansistring">back to top</a>)</p>