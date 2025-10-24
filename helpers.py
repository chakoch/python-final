
import os
import sys
from constants import SEPARATOR_LENGTH, SEPARATOR_CHAR


def wait_for_key():
    print("\nTryck valfri tangent för att gå tillbaka till huvudmeny...")
    
    # För Mac/Linux
    if sys.platform != 'win32':
        import tty
        import termios
        file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_descriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old_settings)
    # För Windows
    else:
        import msvcrt
        msvcrt.getch()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator():
    print(SEPARATOR_CHAR * SEPARATOR_LENGTH)


def print_header(title):
    print("\n" + SEPARATOR_CHAR * SEPARATOR_LENGTH)
    print(f"  {title}")
    print(SEPARATOR_CHAR * SEPARATOR_LENGTH)


def show_screen_with_header(title):
    clear_screen()
    print_header(title)


def get_valid_threshold():

    try:
        threshold_input = input(f"\nSätt in nivå för alarm (1-100): ").strip()
        threshold = int(threshold_input)
        
        if 1 <= threshold <= 100:
            return threshold
        else:
            print("\n✗ Felaktig input! Ange ett värde mellan 1-100.")
            return None
            
    except ValueError:
        print("\n✗ Felaktig input! Ange en siffra mellan 1-100.")
        return None


def format_percentage(value):
    return f"{value:.1f}%"


def format_storage(used_gb, total_gb):
    return f"({used_gb:.1f} GB av {total_gb:.1f} GB används)"