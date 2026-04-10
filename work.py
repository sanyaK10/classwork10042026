from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
import random

console = Console()

def enter_ramka():
    panel = Panel.fit(
        "[ 1 ] Почати гру\n[ 2 ] Історія ігор\n[ 3 ] Вихід",
        title="Головне меню",
        border_style="cyan"
    )
    console.print(panel)
    choice = Prompt.ask("Ваш вибір", choices=["1", "2", "3"])
    return choice

def play_game():
    gamer_choice = Prompt.ask("Ваш вибір : камінь або ножиці або папір", choices=["камінь", "ножиці", "папір"])
    compucter_choice = random.choice(["камінь","ножиці","папір"])
    if gamer_choice == compucter_choice:
        result = "Нічия"
        color = "yellow"
    elif gamer_choice == "камінь" and compucter_choice == "папір":
        result = "Програш"
        color = "red"
    elif gamer_choice == "папір" and compucter_choice == "ножиці":
        result = "Програш"
        color = "red"
    elif gamer_choice == "ножиці" and compucter_choice == "камінь":
        result = "Програш"
        color = "red"
    else:
        result = "Перемога"
        color = "green"

    console.print(f"Результат: {result}", style=color, justify="center")

def games_history():
    console.print("Історія ще не реалізована", style="bold red")

while True:
    choice = enter_ramka()
    match choice:
        case "1":
            play_game()
        case "2":
            games_history()
        case "3":
            console.print("Бувай, на все добре!", style="bold magenta")
            break
