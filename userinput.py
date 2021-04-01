from output import *
from textblob import TextBlob


def GetInput():
    """Get input from the user.

    Gets input from the user and returns the input."""

    return input("\nEnter your selection: ")


def CaptureTextFromTheUser(prompt="Enter some text: "):
    """Captures text from the user.

    Default prompt is "Enter some text: " passing another string makes it the prompt."""

    clear_screen()
    prompt += "\n"
    return TextBlob(input(prompt))
