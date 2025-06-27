# utils/banner.py

from colorama import Fore, Style, init
import time
import shutil
from wcwidth import wcswidth

init(autoreset=True)

def visual_center(text: str, width: int) -> str:
    padding = width - wcswidth(text)
    left = padding // 2
    right = padding - left
    return " " * left + text + " " * right

def print_banner(title: str, width: int = 60, animate: bool = False):
    term_width = shutil.get_terminal_size().columns
    final_width = min(width, term_width - 2)
    margin = (term_width - final_width) // 2 if term_width > final_width else 0
    indent = " " * margin

    # Colors
    border_color_1 = Fore.MAGENTA + Style.BRIGHT
    border_color_2 = Fore.GREEN + Style.BRIGHT
    text_color = Fore.YELLOW + Style.BRIGHT
    edge_color = Fore.BLUE + Style.BRIGHT

    border_top = f"{indent}{edge_color}╔{border_color_1}{'═' * (final_width - 2)}{edge_color}╗"
    border_bottom = f"{indent}{edge_color}╚{border_color_2}{'═' * (final_width - 2)}{edge_color}╝"
    banner_line = visual_center(title, final_width - 2)
    banner_text = f"{indent}{edge_color}║{text_color}{banner_line}{edge_color}║"

    if animate:
        for part in [border_top, banner_text, border_bottom]:
            print(part)
            time.sleep(0.08)
    else:
        print("\n" + border_top)
        print(banner_text)
        print(border_bottom + "\n")
