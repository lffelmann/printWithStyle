<h1>printWithStyle</h1>

Style your print.

<h2>Module</h2>

``printWithStyle(text, bold=False, italic=False, underline=False, foreground=None, background=None)``

<i>text:</i> text to print<br>
Has to be str or list[str] (if list[str] is used every element of the list in a line).

<i>bold:</i> style the text bold<br>
Has to be bool.

<i>italic:</i> style the text italic<br>
Has to be bool.

<i>underline:</i> style the text underline<br>
Has to be bool.

<i>foreground:</i> foreground color<br>
Has to be str. (possible values: "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")

<i>background:</i> background color<br>
Has to be str. (possible values: "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")

<h2>Usage</h2>

```python
from printWithStyle import *
printWithStyle(["Hello","World"], bold=True)
```
<i>Output:</i><br>
<b>Hello<br>World</b>
