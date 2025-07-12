from BaseClasses import ItemClassification as IC, Item
from typing import NamedTuple, Dict
from . import names


class ItemData(NamedTuple):
    classification: IC
    id_number: int
    count: int


class MinecraftItem(Item):
    game = "Minecraft"


important_item_table: Dict[int, ItemData] = {
    names.archery: ItemData(IC.progression, 45000, 1),
    names.resource_crafting: ItemData(IC.progression, 45001, 2),
    # names.resource_blocks: ItemData(IC.progression, 45002, 0),  # Seems to be deprecated
    names.brewing: ItemData(IC.progression, 45003, 1),
    names.enchanting: ItemData(IC.progression, 45004, 1),
    names.bucket: ItemData(IC.progression, 45005, 1),
    names.flint_and_steel: ItemData(IC.progression, 45006, 1),
    names.beds: ItemData(IC.progression, 45007, 1),
    names.bottles: ItemData(IC.progression, 45008, 1),
    names.shield: ItemData(IC.progression, 45009, 1),
    names.fishing: ItemData(IC.progression, 45010, 1),
    names.campfires: ItemData(IC.progression, 45011, 1),
    names.weapons: ItemData(IC.progression, 45012, 3),
    names.tools: ItemData(IC.progression, 45013, 3),
    names.armor: ItemData(IC.progression, 45014, 2),
    names.netherite_scrap: ItemData(IC.progression, 45015, 2),  # Might want to change the number
    names.channeling: ItemData(IC.progression, 45018, 1),
    names.silk_touch: ItemData(IC.progression, 45019, 1),
    names.sharpness_three: ItemData(IC.useful, 45020, 1),
    names.piercing_four: ItemData(IC.progression, 45021, 1),
    names.looting_three: ItemData(IC.useful, 45022, 1),
    names.infinity: ItemData(IC.useful, 45023, 1),
    names.ender_pearl: ItemData(IC.progression, 45029, 4),  # Maybe make an option to add extra Ender Pearls
    names.saddle: ItemData(IC.progression, 45036, 1),
    names.compass_village: ItemData(IC.progression, 45037, 0),
    names.compass_pillager_outpost: ItemData(IC.progression, 45038, 0),
    names.compass_fortress: ItemData(IC.progression, 45039, 0),
    names.compass_bastion_remnant: ItemData(IC.progression, 45040, 0),
    names.compass_end_city: ItemData(IC.progression, 45041, 0),
    names.dragon_egg_shard: ItemData(IC.progression_skip_balancing, 45043, 0),
    names.spyglass: ItemData(IC.progression, 45044, 1),
    names.lead: ItemData(IC.progression, 45045, 1),
    # names.brush: ItemData(IC.progression, 45046, 1),  # Stuff I want to add
    # names.shears: ItemData(IC.progression, 45047, 1),
}

filler_item_table: Dict[int, ItemData] = {
    names.eight_emerald: ItemData(IC.filler, 45016, 0),
    names.four_emerald: ItemData(IC.filler, 45017, 0),
    names.diamond_ore: ItemData(IC.filler, 45024, 0),
    names.iron_ore: ItemData(IC.filler, 45025, 0),
    names.five_hundred_experience: ItemData(IC.filler, 45026, 0),
    names.one_hundred_experience: ItemData(IC.filler, 45027, 0),
    names.fifty_experience: ItemData(IC.filler, 45028, 0),
    names.lapis_lazuli: ItemData(IC.filler, 45030, 0),
    names.cooked_porkchop: ItemData(IC.filler, 45031, 0),
    names.gold_ore: ItemData(IC.filler, 45032, 0),
    names.rotten_flesh: ItemData(IC.filler, 45033, 0),
    names.the_arrow: ItemData(IC.filler, 45034, 0),
    names.thirty_two_arrow: ItemData(IC.filler, 45035, 0),
    names.shulker_box: ItemData(IC.filler, 45042, 0),
    # names.firework_rocket: ItemData(IC.filler, 45048, 0),  # Might add this
}

trap_item_table: Dict[int, ItemData] = {
    names.trap_bees: ItemData(IC.trap, 45100, 0),
}

filler_item_weights = {
    names.eight_emerald: 0,
    names.four_emerald: 1,
    names.diamond_ore: 1,
    names.iron_ore: 1,
    names.five_hundred_experience: 0,
    names.one_hundred_experience: 0,
    names.fifty_experience: 1,
    names.lapis_lazuli: 0,
    names.cooked_porkchop: 1,
    names.gold_ore: 1,
    names.rotten_flesh: 1,
    names.the_arrow: 0,
    names.thirty_two_arrow: 1,
    names.shulker_box: 0,
    # names.firework_rocket: 1,
}

item_table = {
    **important_item_table,
    **filler_item_table,
    **trap_item_table,
}

lookup_item_to_id: Dict[str, int] = {item_name: data.id_number for item_name, data in item_table.items()}
