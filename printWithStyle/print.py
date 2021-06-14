from typing import Union, List

foregroundDict: dict = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"
}

backgroundDict: dict = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47"
}


def printWithStyle(text: Union[str, List[str]], bold: bool = False, italic: bool = False, underline: bool = False,
                   foreground: str = None, background: str = None) -> None:
    """
    Print text in multiple lines with style.

    :param text: Text to print. If list, each element will be one line.
    :type text: Union[str, List[str]]
    :param bold: Print text bold.
    :type bold: bool
    :param italic: Print text italic.
    :type italic: bool
    :param underline: Print text underline.
    :type underline: bool
    :param foreground: Foreground color. ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
    :type foreground: str
    :param background: Background color. ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
    :type background: str
    :rtype: None
    """
    try:
        txt_to_print: str = ""

        if isinstance(text, str):
            txt_to_print = text
        elif isinstance(text, list):
            for i in range(0, len(text)):
                if isinstance(text[i], str):
                    txt_to_print += text[i] + "\n"
                else:
                    raise Exception("Type of text isn't str or List[str].")
            txt_to_print = txt_to_print[:-1]
        else:
            raise Exception("Type of text isn't str or List[str].")

        style: str = "\033["

        if bold is True:
            style += "1;"
        if italic is True:
            style += "3;"
        if underline is True:
            style += "4;"

        if foreground is not None:
            if foreground in foregroundDict:
                style += foregroundDict[foreground] + ";"
            else:
                raise Exception("Foreground color is unknown.")

        if background is not None:
            if background in backgroundDict:
                style += backgroundDict[background] + ";"
            else:
                raise Exception("Background color is unknown.")

        style = style[:-1] + "m"

        print(style + txt_to_print + "\033[0m")
    except:
        raise
