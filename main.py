# Richie Hatch
# MS548 - Module 2 - Due 3/21/2021
# Estimate - 6 hours /  hours actual
# 3/30/2021 - 1 hours
# 3/31/2021 - 2 hours


# used to exit the application
import sys

# requirement from the assignment
from textblob import Word

import menu
from userinput import *
from formatting import *


def ExtractAndPrintNouns(text, title):
    """Extracts the nouns and prints them.

    Given some text extract the nouns and print them."""

    clear_screen()
    PrintHeader(title)
    print("Here are the nouns: \n")
    for noun in text.noun_phrases:
        print(noun)

    print_footer(title)


def ExtractAndPrintSentiment(text, title):
    """Prints the sentiment of the provided text.

    Given the polarity of the statement, one of three states is returned."""

    clear_screen()
    PrintHeader(title)
    print("Here is what you provided: " + text.string)
    print("This is the sentiment: ", end=" ")
    if text.sentiment.polarity < .4:
        print("Woah! That's pretty negative.")
    elif .4 <= text.sentiment.polarity < .6:
        print("That's a relatively neutral statement.")
    else:
        print("That's really positive!")

    print_footer(title)


def ExtractAndPrintWordTags(text, title):
    PrintHeader(title)
    tags = text.tags
    tag_list = []

    for tag in tags:
        if tag[1] not in tag_list:
            tag_list.append(tag[1])

    for tagName in tag_list:
        print(tagName + ": ", end=" ")
        word_list = []
        for tag in tags:
            if tag[1] == tagName:
                word_list.append(tag[0])
        for word in word_list:
            if word_list.index(word) == len(word_list) - 1:
                print(word + ".")
            else:
                print(word + ",", end=" ")

    print_footer(title)


def PluralizeAndPrint(text, title):
    PrintHeader(title)
    for word in text.words:
        w = Word(word)
        print(w.pluralize())

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
