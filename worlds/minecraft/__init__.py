from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld


# TODO: Write new setup guides
class MinecraftWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Minecraft randomizer connected to an Archipelago multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TBD"]
    )]
