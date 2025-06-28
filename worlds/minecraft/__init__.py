from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from .items import item_table
from . import names


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


class MinecraftWorld(World):
    """
    Minecraft is a game about building, exploring, fighting, and the titular mining and crafting.
    Complete Advancements to be rewarded items as you make your way to the End to fight the Ender Dragon.
    """
    game = "Minecraft"
    web = MinecraftWeb()

    item_name_to_id = {data.name: item_id for item_id, data in items.item_table.items()}
