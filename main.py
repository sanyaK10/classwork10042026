from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title = "список студентів")
table.add_column("Імя",style = "cyan")
table.add_column("Курсовий проект",style = "magenta")

table.add_row("Антон","чат-бот")
table.add_row("Марія","гра на пайтон")

console.print(table)


# import cowsay

# from art import*

# # tprint("Hello")
# # randart()

# art_text = text2art("Hello",font="block",chr_ignore=True)
# # print(art_text)
# tprint("test","rind-xlarge")

# cowsay.cow("Hello!")
# cowsay.dragon("Hello,i am dragon")
# cowsay.octopus("Hello,i am octopus")
# cowsay.trex("RAAAAAAAAAAAAAA")
# cowsay.stegosaurus("usiiiiiiiiirwe")





