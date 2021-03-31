from os import system


def clear_screen():
    system("cls")


def PrintHeader(header):
    print("--------" + header + "--------")


def print_footer(footer):
    footer_count = ""
    for char in footer:
        footer_count += "-"
    print("--------" + footer_count + "--------")
    input("Press ENTER to continue.")
    clear_screen()
