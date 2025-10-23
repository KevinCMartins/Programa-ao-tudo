# Alternative version using the Rich library for better colors
import sys
from time import sleep
from rich.console import Console

def printLyrics():
    console = Console()
    
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("come on, come on", 0.035),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("come on, come on", 0.035),
        ("Rock that body", 0.08),
    ]

    delays = [0.2, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5]
    
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == '(Rock your body)':
                console.print(char, style="orange4", end='')
            else:
                console.print(char, style="bold gold3", end='')
            sleep(char_delay)
        console.print()  # New line
        
        if i < len(delays):
            sleep(delays[i])

if __name__ == "__main__":
    printLyrics()
