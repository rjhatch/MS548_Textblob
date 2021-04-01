# Richie Hatch
# MS548 - Module 2 - Due 3/21/2021
# Estimate - 6 hours / 5 hours actual
# 3/30/2021 - 1 hours
# 3/31/2021 - 4 hours
# There was a ton of refactoring in this iteration. The functionality of the dictionary and writing to a file
# really wasn't too difficult. Breaking apart the program for it to be easier to extent was the more difficult portion.


# used to exit the application
import sys

# requirement from the assignment
from textblob import Word

import menu
from userinput import *
from output import *


def ExtractAndPrintNouns(text, title):
    """Extracts the nouns and prints them.

    Given some text extract the nouns and print them."""

    clear_screen()
    PrintHeader(title)

    print_and_write("Here is what you provided: " + text.string)

    print_and_write("Here are the nouns: \n")
    for noun in text.noun_phrases:
        print_and_write(noun)

    print_footer(title)


def ExtractAndPrintSentiment(text, title):
    """Prints the sentiment of the provided text.

    Given the polarity of the statement, one of three states is returned."""

    clear_screen()
    PrintHeader(title)
    print_and_write("Here is what you provided: " + text.string)
    print_and_write("This is the sentiment: ", end=" ")
    if text.sentiment.polarity < .4:
        print_and_write("Woah! That's pretty negative.")
    elif .4 <= text.sentiment.polarity < .6:
        print_and_write("That's a relatively neutral statement.")
    else:
        print_and_write("That's really positive!")

    print_footer(title)


def ExtractAndPrintWordTags(text, title):
    PrintHeader(title)
    tags = text.tags
    tag_list = []

    print_and_write("Here is what you provided: " + text.string)

    for tag in tags:
        if tag[1] not in tag_list:
            tag_list.append(tag[1])

    for tagName in tag_list:
        print_and_write(tagName + ": ", end=" ")
        word_list = []
        for tag in tags:
            if tag[1] == tagName:
                word_list.append(tag[0])
        for word in word_list:
            if word_list.index(word) == len(word_list) - 1:
                print_and_write(word + ".")
            else:
                print_and_write(word + ",", end=" ")

    print_footer(title)


def PluralizeAndPrint(text, title):
    PrintHeader(title)

    print_and_write("Here is what you provided: " + text.string)

    for word in text.words:
        w = Word(word)
        print_and_write(w.pluralize())

    print_footer(title)


menu = menu.Menu()
menu.add_menu_item("Sentiment", "Provide the sentiment for a selection of text.",
                   "Enter text, let's see if I can figure out if it's positive or negative.", ExtractAndPrintSentiment)
menu.add_menu_item("The Nouns", "Pick out the nouns from a selection of text.",
                   "Enter text, include nouns so I can pick them out!", ExtractAndPrintNouns)
menu.add_menu_item("Word Tags", "Breakdown text by word type.",
                   "Enter text, I'll tell you what each word is.", ExtractAndPrintWordTags)
menu.add_menu_item("Pluralize", "Pluralize.",
                   "Enter text, I'll pluralize it.", PluralizeAndPrint)


while 1:
    # Menu()
    menu.display_menu()
    # HandleInput(GetInput())
    if menu.call_menu_item(GetInput()) == "QUIT":
        sys.exit()
