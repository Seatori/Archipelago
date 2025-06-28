from BaseClasses import ItemClassification as IC
from typing import NamedTuple, Dict
from . import names


class ItemData(NamedTuple):
    classification: IC
    count: int


base_id = 1

item_table: Dict[int, ItemData] = {
    names.archery: ItemData(IC.progression, 1),
    names.resource_crafting: ItemData(IC.progression, 2),
    # names.resource_blocks: ItemData(IC.progression, 0),  # Seems to be deprecated
    names.brewing: ItemData(IC.progression, 1),
    names.enchanting: ItemData(IC.progression, 1),
    names.bucket: ItemData(IC.progression, 1),
    names.flint_and_steel: ItemData(IC.progression, 1),
    names.beds: ItemData(IC.progression, 1),
    names.bottles: ItemData(IC.progression, 1),
    names.shield: ItemData(IC.progression, 1),
    names.fishing: ItemData(IC.progression, 1),
    names.campfires: ItemData(IC.progression, 1),
    names.weapons: ItemData(IC.progression, 3),
    names.tools: ItemData(IC.progression, 3),
    names.armor: ItemData(IC.progression, 2),
    names.netherite_scrap: ItemData(IC.progression, 2),  # Might want to change the number
    names.eight_emerald: ItemData(IC.filler, 0),
    names.four_emerald: ItemData(IC.filler, 0),
    names.channeling: ItemData(IC.progression, 1),
    names.silk_touch: ItemData(IC.progression, 1),
    names.sharpness_three: ItemData(IC.useful, 1),
    names.piercing_four: ItemData(IC.progression, 1),
    names.looting_three: ItemData(IC.useful, 1),
    names.infinity: ItemData(IC.useful, 1),
    names.diamond_ore: ItemData(IC.filler, 0),
    names.iron_ore: ItemData(IC.filler, 0),
    names.five_hundred_experience: ItemData(IC.filler, 0),
    names.one_hundred_experience: ItemData(IC.filler, 0),
    names.fifty_experience: ItemData(IC.filler, 0),
    names.ender_pearl: ItemData(IC.progression, 4),  # Maybe make an option to add extra Ender Pearls
    names.lapis_lazuli: ItemData(IC.filler, 0),
    names.cooked_porkchop: ItemData(IC.filler, 0),
    names.gold_ore: ItemData(IC.filler, 0),
    names.rotten_flesh: ItemData(IC.filler, 0),
    names.the_arrow: ItemData(IC.filler, 0),
    names.thirty_two_arrow: ItemData(IC.filler, 0),
    names.saddle: ItemData(IC.progression, 1),
    names.compass_village: ItemData(IC.progression, 0),
    names.compass_pillager_outpost: ItemData(IC.progression, 0),
    names.compass_fortress: ItemData(IC.progression, 0),
    names.compass_bastion_remnant: ItemData(IC.progression, 0),
    names.compass_end_city: ItemData(IC.progression, 0),
    names.shulker_box: ItemData(IC.filler, 0),
    names.dragon_egg_shard: ItemData(IC.progression, 0),
    names.spyglass: ItemData(IC.progression, 1),
    names.lead: ItemData(IC.progression, 1),
    # names.brush: ItemData(IC.progression, 1),  # Stuff I want to add
    # names.shears: ItemData(IC.progression, 1),
    # names.firework_rocket: ItemData(IC.filler, 0),
    names.trap_bees: ItemData(IC.trap, 0),
}
