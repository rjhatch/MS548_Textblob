# Richie Hatch
# MS548 - Module 2 - Due 3/21/2021
# Estimate - 2 hours / 2 hours actual
# 4/9/2021 - 2 hours
# I was able to hit the projected time.


# used to exit the application
import sys

# requirement from the assignment
from textblob import Word, TextBlob

import menu
from userinput import *
from output import *


def extract_and_print_nouns(text, title):
    """Extracts the nouns and prints them.

    Given some text extract the nouns and print them."""

    clear_screen()
    print_header(title)

    print_and_write("Here is what you provided: " + text.string)

    print_and_write("Here are the nouns: \n")
    for noun in text.noun_phrases:
        print_and_write(noun)

    print_footer(title)


def extract_and_print_sentiment(text, title):
    """Prints the sentiment of the provided text.

    Given the polarity of the statement, one of three states is returned."""

    clear_screen()
    print_header(title)
    print_and_write("Here is what you provided: " + text.string)
    print_and_write("This is the sentiment: ", end=" ")
    if text.sentiment.polarity < .4:
        print_and_write("Woah! That's pretty negative.")
    elif .4 <= text.sentiment.polarity < .6:
        print_and_write("That's a relatively neutral statement.")
    else:
        print_and_write("That's really positive!")

    print_footer(title)


def extract_and_print_word_tags(text, title):
    """Helper method to write to a file and display to the screen.

    Get use end= to determine what the end of the string is."""
    print_header(title)
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


def pluralize_and_print(text, title):
    """Pluralize the given text

    Pluralize and print the given text."""
    print_header(title)

    print_and_write("Here is what you provided: " + text.string)

    for word in text.words:
        w = Word(word)
        print_and_write(w.pluralize())

    print_footer(title)


def correct_spelling(text, title):
    """Correct spelling of the given text

    Corrects and prints the text provided."""
    print_header(title)

    print_and_write("Here is what you provided: " + text.string)

    print_and_write(text.correct())

    print_footer(title)


def word_and_noun_frequencies(text, title):
    """Print how many times a word appears.

    Given text and a word print how many times the word appears."""
    print_header(title)

    print_and_write("Here is what you provided: " + text.string)

    word_choice = input("\nEnter a word and I'll find the frequency: ")

    print_and_write("You want me to find the frequency of the word: " + word_choice)

    print_and_write(text.word_counts[word_choice])

    print_footer(title)


def check_spelling(text, title):
    """Check for spelling errors.

    Given text, check the spelling and print the probability of word suggestions."""
    print_header(title)

    print_and_write("Here is what you provided: " + text.string)

    print_and_write("Here is the probability of correct spelling and suggestions if needed: ")

    # tokenization from the text blob library
    words = text.words

    for word in words:
        print_and_write(Word(word).spellcheck())

    print_footer(title)


menu = menu.Menu()
menu.add_menu_item("Sentiment", "Provide the sentiment for a selection of text.",
                   "Enter text, let's see if I can figure out if it's positive or negative.",
                   extract_and_print_sentiment)
menu.add_menu_item("The Nouns", "Pick out the nouns from a selection of text.",
                   "Enter text, include nouns so I can pick them out!", extract_and_print_nouns)
menu.add_menu_item("Word Tags", "Breakdown text by word type.",
                   "Enter text, I'll tell you what each word is.", extract_and_print_word_tags)
menu.add_menu_item("Pluralize", "Pluralize.",
                   "Enter text, I'll pluralize it.", pluralize_and_print)
menu.add_menu_item("Word Frequency", "Check word frequency",
                   "Enter a sentence or sentences and then I'll ask for a word to check.", word_and_noun_frequencies)
menu.add_menu_item("Spell Check", "Check Spelling",
                   "Enter text and I'll check the spelling of each word.", check_spelling)
menu.add_menu_item("Correct Spelling", "Correct Spelling",
                   "Enter text and I'll try to correct any spelling mistakes.", correct_spelling)

while 1:
    # Menu()
    menu.display_menu()
    # HandleInput(GetInput())
    if menu.call_menu_item(GetInput()) == "QUIT":
        sys.exit()
