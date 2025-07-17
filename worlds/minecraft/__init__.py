import logging
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld, CollectionState
from worlds.AutoWorld import WebWorld, World

logger = logging.getLogger(__name__)

MINECRAFT = "Minecraft"
# UNIVERSAL_TRACKER_SEED_PROPERTY = "ut_seed" Something to look into?

client_version = 1


class MinecraftLocation(Location):
    game: str = MINECRAFT


class MinecraftItem(Item):
    game: str = MINECRAFT


# TODO: Write new setup guides
class MinecraftWeb(WebWorld):
    theme = "dirt"
    bug_report_page = "https://github.com/qixils/NeoForgeAP"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Minecraft randomizer connected to an Archipelago multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TBD"]
    )]


# TODO: Rewrite MinecraftWorld
class MinecraftWorld(World):
    """
    Minecraft is a sandbox game made out of cubes. Mine ores, craft items, fight mobs and bosses, explore structures and
     dimensions, and build ANYTHING in a procedurally generated world. Just don't get exploded by a creeper...
    """

