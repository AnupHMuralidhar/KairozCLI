from colorama import Fore, Style, init
import time
from wcwidth import wcswidth

init(autoreset=True)

def visual_center(text: str, width: int = 60) -> str:
    padding = width - wcswidth(text)
    left = padding // 2
    right = padding - left
    return " " * left + text + " " * right

def print_feature_banner(title: str, animate: bool = False, width: int = 60):
    """
    Prints a stylish header for Kairoz feature modules like Analyze, Monitor, etc.
    """
    arrow = f"{Fore.MAGENTA}{Style.BRIGHT}>>"
    label = f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT} {title} "
    underline = f"{Fore.MAGENTA}{Style.DIM}" + "═" * width

    if animate:
        print()
        for line in [arrow + label]:
            print(line)
            time.sleep(0.05)
        print(underline)
        print()
    else:
        print()
        print(arrow + label)
        print(underline)
        print()
