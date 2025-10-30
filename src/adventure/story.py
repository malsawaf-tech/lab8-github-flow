from adventure.utils import read_events_from_file
import random
from rich import print

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[red]You stand still, unsure what to do. The forest swallows you.[/red]"

def left_path(event):
    return "[green]You walk left. [/green]" + event

def right_path(event):
    return "[blue]You walk right. [/blue]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[dark_blue]You wake up in a dark forest. You can go left or right.[/dark_blue]")
    while True:
        print("[gray37]Which direction do you choose?[/gray37] ([green]left[/green]/[blue]right[/blue]/[red]exit[/red]): ",end="")
        choice = input()
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
