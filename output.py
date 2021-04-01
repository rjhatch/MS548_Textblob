from os import system
from fileoperations import FileWrite


def clear_screen():
    system("cls")


def PrintHeader(header):
    print_and_write("--------" + header + "--------")


def print_footer(footer):
    footer_count = ""
    for char in footer:
        footer_count += "-"
    print_and_write("--------" + footer_count + "--------")
    input("Press ENTER to continue.")
    clear_screen()


def print_and_write(statement, end="\n"):
    print(statement, end=end)
    write_file = FileWrite("output.txt")
    write_file.file_append(statement + end)
