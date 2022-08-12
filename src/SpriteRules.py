from typing import NamedTuple, Tuple, Union, TYPE_CHECKING

from SpriteConstants import SpriteConstants
from DungeonRoomConstants import RoomConstants
from SpecialRoomRules import *


class SpriteRules(NamedTuple):
    overlord: bool = False
    boss: bool = False
    randomize: bool = True
    killable: bool = False
    npc: bool = False
    never_use_dungeon: bool = False
    never_use_overworld: bool = False
    cannot_have_key: bool = False
    is_object: bool = False
    absorbable: bool = False
    is_water_sprite: bool = False
    is_enemy_sprite: bool = True
    group_id: Union[Tuple, int] = None
    sub_group0: Union[Tuple, int] = None
    sub_group1: Union[Tuple, int] = None
    sub_group2: Union[Tuple, int] = None
    sub_group3: Union[Tuple, int] = None
    excluded_rooms: set[int] = set()
    do_not_randomize_rooms: set[int] = set()
    spawnable_rooms: set[int] = set()


SPRITE_RULES: dict[int, SpriteRules] = {
    SpriteConstants.raven:                      SpriteRules(cannot_have_key=True, sub_group3=(17, 25), excluded_rooms=DONT_USE_FLYING_SPRITES),
    SpriteConstants.vulture:                    SpriteRules(cannot_have_key=True, sub_group2=18, excluded_rooms=DONT_USE_FLYING_SPRITES),

    # SpriteConstants.flying_stalfos_head:        SpriteRules(),  # TODO not sure why this is commented out?
    SpriteConstants.empty:                      SpriteRules(never_use_dungeon=True, never_use_overworld=True),

    SpriteConstants.pull_switch_good:           SpriteRules(randomize=False, is_object=True, never_use_overworld=True, never_use_dungeon=True, sub_group3=(82, 83)),
    SpriteConstants.pull_switch_trap:           SpriteRules(randomize=False, is_object=True, never_use_dungeon=True, never_use_overworld=True, sub_group3=(82, 83)),

    SpriteConstants.octorok_one_way:            SpriteRules(killable=True, sub_group2=(12, 24)),
    SpriteConstants.moldorm:                    SpriteRules(boss=True, sub_group2=48),
    SpriteConstants.octorok_four_way:           SpriteRules(killable=True, sub_group2=12),

    SpriteConstants.cucco:                      SpriteRules(sub_group3=(21, 80), excluded_rooms=DONT_USE_FLYING_SPRITES),
    SpriteConstants.buzzblob:                   SpriteRules(cannot_have_key=True, killable=True, sub_group3=17, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.snap_dragon:                SpriteRules(killable=True, sub_group0=22, sub_group2=23),

    SpriteConstants.octo_balloon:               SpriteRules(cannot_have_key=True, sub_group2=12, excluded_rooms=DONT_USE_FLYING_SPRITES),
    SpriteConstants.octo_balloon_hatchlings:    SpriteRules(never_use_dungeon=True, never_use_overworld=True, sub_group2=12),

    SpriteConstants.hinox:                      SpriteRules(killable=True, sub_group0=22),
    SpriteConstants.moblin:                     SpriteRules(killable=True, sub_group2=23),

    SpriteConstants.mini_helmasaur:             SpriteRules(killable=True, sub_group1=30),
    SpriteConstants.gargoyles_domain_gate:      SpriteRules(randomize=False, is_object=True, never_use_dungeon=True, never_use_overworld=True),
    SpriteConstants.anti_fairy:                 SpriteRules(sub_group3=(82, 83),
                                                            excluded_rooms=DONT_USE_FLYING_SPRITES | {RoomConstants.agahnims_tower_final_bridge}),  # final bridge could require powder

    SpriteConstants.sahasrahla_aginah:          SpriteRules(npc=True, sub_group2=76),

    SpriteConstants.bush_hoarder:               SpriteRules(cannot_have_key=True, killable=True, sub_group3=17, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.mini_moldorm:               SpriteRules(killable=True, sub_group1=30),
    SpriteConstants.poe:                        SpriteRules(cannot_have_key=True, sub_group3=(14, 21), excluded_rooms=DONT_USE_FLYING_SPRITES),

    SpriteConstants.dwarves:                    SpriteRules(npc=True, randomize=False, sub_group1=77, sub_group3=21),
    SpriteConstants.arrow_in_wall_maybe:        SpriteRules(randomize=False, never_use_overworld=True, never_use_dungeon=True),
    SpriteConstants.statue:                     SpriteRules(randomize=False, is_object=True, sub_group3=(82, 83),
                                                            excluded_rooms=DONT_USE_IMMOVABLE_SPRITES | {RoomConstants.ice_palace_map_chest}),
    SpriteConstants.weathervane:                SpriteRules(randomize=False, never_use_overworld=True, never_use_dungeon=True),
    SpriteConstants.crystal_switch:             SpriteRules(randomize=False, is_object=True, never_use_dungeon=True, never_use_overworld=True, sub_group3=83),
    SpriteConstants.bug_catching_kid:           SpriteRules(randomize=False, npc=True, sub_group0=81),

    SpriteConstants.sluggula:                   SpriteRules(sub_group2=37),
    SpriteConstants.push_switch:                SpriteRules(randomize=False, is_object=True, never_use_overworld=True, never_use_dungeon=True, sub_group3=83),

    SpriteConstants.ropa:                       SpriteRules(killable=True, sub_group0=22),
    SpriteConstants.red_bari:                   SpriteRules(killable=True, cannot_have_key=True, sub_group0=31, do_not_randomize_rooms={RoomConstants.ice_palace_big_spike_traps}),
    SpriteConstants.blue_bari:                  SpriteRules(killable=True, sub_group0=31, do_not_randomize_rooms={RoomConstants.ice_palace_big_spike_traps}),

    SpriteConstants.talking_tree:               SpriteRules(npc=True, randomize=False, sub_group0=21),

    SpriteConstants.hardhat_beetle:             SpriteRules(sub_group1=30),
    SpriteConstants.deadrock:                   SpriteRules(sub_group3=16, excluded_rooms={RoomConstants.ice_palace_big_spike_traps, RoomConstants.mimic_cave}),

    SpriteConstants.storytellers:               SpriteRules(npc=True, randomize=False),
    SpriteConstants.blind_hideout_attendant:    SpriteRules(npc=True, randomize=False, sub_group0=(14, 79)),
    SpriteConstants.sweeping_lady:              SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.multipurpose_sprite:        SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.lumberjacks:                SpriteRules(npc=True, randomize=False, sub_group2=74),
    SpriteConstants.telepathic_stones_no_idea_what_this_actually_is_likely_unused:  SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.flute_boys_notes:           SpriteRules(randomize=False, never_use_overworld=True, never_use_dungeon=True),
    SpriteConstants.race_hp_npcs:               SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.person_maybe:               SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.fortune_teller:             SpriteRules(npc=True, randomize=False, sub_group0=75),
    SpriteConstants.angry_brothers:             SpriteRules(npc=True, randomize=False, sub_group0=79),
    SpriteConstants.pull_for_rupees:            SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.scared_girl_2:              SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.innkeeper:                  SpriteRules(npc=True, randomize=False),
    SpriteConstants.witch:                      SpriteRules(npc=True, randomize=False, sub_group2=76),
    SpriteConstants.waterfall:                  SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False),
    SpriteConstants.arrow_target:               SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.average_middle_aged_man:    SpriteRules(npc=True, randomize=False, sub_group3=17),
    SpriteConstants.half_magic_bat:             SpriteRules(npc=True, randomize=False, sub_group3=17),
    SpriteConstants.dash_item:                  SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False),
    SpriteConstants.village_kid:                SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.signs_chicken_lady_also_showed_up_scared_ladies_outside_houses: SpriteRules(npc=True, randomize=False, group_id=6),

    SpriteConstants.rock_hoarder:               SpriteRules(sub_group3=17, excluded_rooms={RoomConstants.mimic_cave}),

    SpriteConstants.tutorial_soldier:           SpriteRules(npc=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.lightning_lock:             SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=63),

    SpriteConstants.blue_sword_soldier_detect_player:   SpriteRules(killable=True, sub_group1=(13, 73)),
    SpriteConstants.green_sword_soldier:        SpriteRules(killable=True, sub_group1=73),
    SpriteConstants.red_spear_soldier:          SpriteRules(killable=True, sub_group1=(13, 73)),
    SpriteConstants.assault_sword_soldier:      SpriteRules(killable=True, sub_group0=70, sub_group1=73),
    SpriteConstants.green_spear_soldier:        SpriteRules(killable=True, sub_group1=(13, 73)),
    SpriteConstants.blue_archer:                SpriteRules(killable=True, sub_group0=72, sub_group1=73),
    SpriteConstants.green_archer:               SpriteRules(killable=True, sub_group0=72, sub_group1=73),
    SpriteConstants.red_javelin_soldier:        SpriteRules(killable=True, sub_group0=70, sub_group1=73),
    SpriteConstants.red_javelin_soldier_2:      SpriteRules(killable=True, sub_group0=70, sub_group1=73),
    SpriteConstants.red_bomb_soldiers:          SpriteRules(killable=True, sub_group0=70, sub_group1=73),
    SpriteConstants.green_soldier_recruits_hm_knight:   SpriteRules(killable=True, sub_group1=73, sub_group2=19),

    SpriteConstants.geldman:                    SpriteRules(killable=True, cannot_have_key=True, sub_group2=18, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.rabbit:                     SpriteRules(sub_group3=17),
    SpriteConstants.popo:                       SpriteRules(killable=True, sub_group1=44),
    SpriteConstants.popo_2:                     SpriteRules(killable=True, sub_group1=44),

    SpriteConstants.cannon_balls:               SpriteRules(randomize=False, never_use_dungeon=True, never_use_overworld=True, sub_group2=46),
    SpriteConstants.armos:                      SpriteRules(killable=True, sub_group3=16, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.giant_zora:                 SpriteRules(npc=True, randomize=False, sub_group3=68),

    SpriteConstants.armos_knights:              SpriteRules(boss=True, sub_group3=29),
    SpriteConstants.lanmolas:                   SpriteRules(boss=True, sub_group3=49),
    SpriteConstants.fireball_zora:              SpriteRules(is_water_sprite=True, sub_group2=(12, 24)),
    SpriteConstants.walking_zora:               SpriteRules(is_water_sprite=True, cannot_have_key=True, killable=True, sub_group2=12, sub_group3=68),
    SpriteConstants.desert_palace_barriers:     SpriteRules(never_use_overworld=True, never_use_dungeon=True, sub_group2=18),
    SpriteConstants.crab:                       SpriteRules(killable=True, sub_group2=12),
    SpriteConstants.bird:                       SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group2=55, sub_group3=54),
    SpriteConstants.squirrel:                   SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False, sub_group2=55, sub_group3=54),
    SpriteConstants.spark_right_to_left:        SpriteRules(sub_group0=31),
    SpriteConstants.spark_left_to_right:        SpriteRules(sub_group0=31),

    # TODO track down sprite positions and exclude these
    SpriteConstants.roller_vertical_moving:     SpriteRules(sub_group2=39, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),
    SpriteConstants.roller_vertical_moving_2:   SpriteRules(sub_group2=39, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),
    SpriteConstants.roller:                     SpriteRules(sub_group2=39, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),
    SpriteConstants.roller_horizontal_moving:   SpriteRules(sub_group2=39, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),
    SpriteConstants.beamos:                     SpriteRules(sub_group1=44, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),

    SpriteConstants.master_sword:               SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group2=55, sub_group3=54),
    # TODO figure out how to add these. they currently overload sprites
    SpriteConstants.devalant_shooter:           SpriteRules(never_use_dungeon=True, never_use_overworld=True, killable=True, sub_group0=47),
    SpriteConstants.devalant_non_shooter:       SpriteRules(never_use_overworld=True, never_use_dungeon=True, killable=True, sub_group0=47),

    SpriteConstants.shooting_gallery_proprietor:    SpriteRules(npc=True, randomize=False, sub_group0=75),
    SpriteConstants.moving_cannon_ball_shooters_up: SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group0=47),
    SpriteConstants.moving_cannon_ball_shooters_right:  SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group0=47),
    SpriteConstants.moving_cannon_ball_shooters_left:   SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group0=47),
    SpriteConstants.moving_cannon_ball_shooters_down:   SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group0=47),

    SpriteConstants.ball_n_chain_trooper:       SpriteRules(killable=True, sub_group0=70, sub_group1=73),
    SpriteConstants.cannon_soldier:             SpriteRules(killable=True, sub_group0=70, sub_group1=73),

    SpriteConstants.mirror_portal:              SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.rat:                        SpriteRules(killable=True, sub_group2=(28, 36)),
    SpriteConstants.rope:                       SpriteRules(killable=True, sub_group2=(28, 36)),
    SpriteConstants.keese:                      SpriteRules(killable=True, cannot_have_key=True, sub_group2=(28, 36)),
    # SpriteConstants.helmasaur_king_fireball:    SpriteRules()
    SpriteConstants.leever:                     SpriteRules(killable=True, sub_group0=47),
    SpriteConstants.activato_for_the_ponds_where_you_throw_in_items:    SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=54),
    SpriteConstants.uncle_priest:               SpriteRules(npc=True, randomize=False, sub_group0=(71, 81)),
    SpriteConstants.running_man:                SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.bottle_salesman:            SpriteRules(npc=True, randomize=False, group_id=6),
    SpriteConstants.princess_zelda:             SpriteRules(npc=True, randomize=False),
    # SpriteConstants.anti_fairy_alternate:       SpriteRules()
    SpriteConstants.village_elder:              SpriteRules(npc=True, randomize=False, sub_group0=75, sub_group1=77, sub_group2=74),
    # SpriteConstants.bee:                        SpriteRules()
    SpriteConstants.agahnim:                    SpriteRules(never_use_dungeon=True, never_use_overworld=True, boss=True, sub_group0=85, sub_group1=(26, 61), sub_group2=66, sub_group3=67),
    SpriteConstants.agahnim_energy_ball:        SpriteRules(never_use_overworld=True, never_use_dungeon=True),
    SpriteConstants.floating_stalfos_head:      SpriteRules(sub_group0=31, excluded_rooms=DONT_USE_FLYING_SPRITES),  # killable?
    SpriteConstants.big_spike_trap:             SpriteRules(sub_group3=(82, 83), excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),
    SpriteConstants.guruguru_bar_clockwise:     SpriteRules(sub_group0=31, excluded_rooms={RoomConstants.turtle_rock_dark_maze, RoomConstants.ganons_tower_torches_1}),
    SpriteConstants.guruguru_bar_counter_clockwise: SpriteRules(sub_group0=31, excluded_rooms={RoomConstants.turtle_rock_dark_maze, RoomConstants.ganons_tower_torches_1}),
    SpriteConstants.winder:                     SpriteRules(sub_group0=31),
    SpriteConstants.water_tektite:              SpriteRules(is_water_sprite=True, sub_group2=34, excluded_rooms={RoomConstants.swamp_palace_entrance} | DONT_USE_FLYING_SPRITES),
    SpriteConstants.anti_fairy_circle:          SpriteRules(never_use_dungeon=True, never_use_overworld=True, sub_group3=(82, 83)),  # laggy
    SpriteConstants.green_eyegore:              SpriteRules(killable=True, sub_group2=46, excluded_rooms={RoomConstants.mimic_cave}), # subgroup1=44, can't be killed with bombs
    SpriteConstants.red_eyegore:                SpriteRules(sub_group2=46), # subgroup1=44
    # SpriteConstants.yellow_stalfos:             SpriteRules(),  # TODO apparently
    SpriteConstants.kodongo:                    SpriteRules(never_use_overworld=True, never_use_dungeon=True, sub_group2=42), # broken asm?
    SpriteConstants.mothula:                    SpriteRules(boss=True, sub_group2=56, sub_group3=82),
    SpriteConstants.mothulas_beam:              SpriteRules(never_use_dungeon=True, never_use_overworld=True, sub_group2=56),
    SpriteConstants.spike_trap:                 SpriteRules(sub_group3=(82, 83), excluded_rooms=DONT_USE_IMMOVABLE_SPRITES | {RoomConstants.swamp_palace_entrance}),
    SpriteConstants.gibdo:                      SpriteRules(killable=True, sub_group2=35),
    SpriteConstants.arrghus:                    SpriteRules(boss=True, sub_group2=57),
    SpriteConstants.arrghus_spawn:              SpriteRules(boss=True, sub_group2=57),
    SpriteConstants.terrorpin:                  SpriteRules(sub_group2=42, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.slime_that_jumps_out_of_the_floor:  SpriteRules(sub_group1=32),
    # these require asm to work on overworld and only work in dungeons with exits
    SpriteConstants.wallmaster:                 SpriteRules(randomize=False, never_use_overworld=True, sub_group2=35, spawnable_rooms=DUNGEON_ROOMS),

    SpriteConstants.stalfos_knight:             SpriteRules(sub_group1=32, excluded_rooms={RoomConstants.mimic_cave}),
    SpriteConstants.helmasaur_king:             SpriteRules(boss=True, sub_group2=58, sub_group3=62),
    SpriteConstants.bumper:                     SpriteRules(never_use_overworld=True, never_use_dungeon=True, is_object=True, randomize=False, sub_group3=(82, 83)),
    SpriteConstants.swimmers_evil:              SpriteRules(is_water_sprite=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),  # TODO

    SpriteConstants.eyelaser_up:                SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=(82, 83)),
    SpriteConstants.eyelaser_down:              SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=(82, 83)),
    SpriteConstants.eyelaser_left:              SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=(82, 83)),
    SpriteConstants.eyelaser_right:             SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=(82, 83)),

    SpriteConstants.pengator:                   SpriteRules(killable=True, sub_group2=38),
    SpriteConstants.kyameron_water_splash:      SpriteRules(is_water_sprite=True, sub_group2=34,
                                                            do_not_randomize_rooms={RoomConstants.swamp_palace_entrance},
                                                            excluded_rooms={RoomConstants.mimic_cave}),

    SpriteConstants.wizzrobe:                   SpriteRules(sub_group2=(37, 41)), # TODO can't be killed with bombs

    SpriteConstants.vermin_vertical:            SpriteRules(randomize=False, cannot_have_key=True, killable=True, sub_group1=32), # keys can get stuck in walls
    SpriteConstants.vermin_horizontal:          SpriteRules(randomize=False, cannot_have_key=True, killable=True, sub_group1=32),

    SpriteConstants.ostrich_haunted_grove:      SpriteRules(never_use_dungeon=True, never_use_overworld=True, sub_group2=78),
    SpriteConstants.flute:                      SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.birds_haunted_grove:        SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False, sub_group2=78),

    SpriteConstants.freezor:                    SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group2=38),  # TODO investigate this is likely due to fire rod req

    SpriteConstants.kholdstare:                 SpriteRules(boss=True, sub_group2=60),
    SpriteConstants.kholdstares_shell:          SpriteRules(boss=True),
    SpriteConstants.falling_ice:                SpriteRules(boss=True, sub_group2=60),

    SpriteConstants.blue_zazak:                 SpriteRules(killable=True, sub_group2=40),
    SpriteConstants.red_zazak:                  SpriteRules(killable=True, sub_group2=40),

    SpriteConstants.stalfos:                    SpriteRules(killable=True, sub_group0=31),

    SpriteConstants.bomber_flying_creatures_from_darkworld: SpriteRules(cannot_have_key=True, sub_group3=27, excluded_rooms=DONT_USE_FLYING_SPRITES),
    SpriteConstants.bomber_flying_creatures_from_darkworld_2: SpriteRules(cannot_have_key=True, sub_group3=27, excluded_rooms=DONT_USE_FLYING_SPRITES),

    SpriteConstants.pikit:                      SpriteRules(cannot_have_key=True, killable=True, sub_group3=27),
    SpriteConstants.maiden:                     SpriteRules(npc=True, randomize=False),
    SpriteConstants.apple:                      SpriteRules(randomize=False, absorbable=True),
    SpriteConstants.lost_old_man:               SpriteRules(npc=True, randomize=False, sub_group0=70, sub_group1=73, sub_group2=28),

    SpriteConstants.down_pipe:                  SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.up_pipe:                    SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.right_pipe:                 SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.left_pipe:                  SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),

    SpriteConstants.good_bee_again_maybe:       SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group0=31),
    SpriteConstants.hylian_inscription:         SpriteRules(is_object=True, never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.thiefs_chest:               SpriteRules(is_object=True, never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=21),
    SpriteConstants.bomb_salesman:              SpriteRules(npc=True, randomize=False, sub_group1=77),
    SpriteConstants.kiki:                       SpriteRules(npc=True, randomize=False, sub_group3=25),
    SpriteConstants.maiden_in_blind_dungeon:    SpriteRules(npc=True, randomize=False),
    SpriteConstants.mimic:                      SpriteRules(sub_group1=44),

    SpriteConstants.feuding_friends_on_death_mountain:  SpriteRules(npc=True, randomize=False, sub_group3=20),
    SpriteConstants.whirlpool:                  SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),

    SpriteConstants.salesman_chest_game_guy_300_rupee_giver_guy_chest_game_thief:
        SpriteRules(npc=True, randomize=False, sub_group0=(75, 79, 14, 21), sub_group1=77, sub_group2=74, sub_group3=90,
                    spawnable_rooms={RoomConstants.cave_0xFF, RoomConstants.cave_shop_0x112, RoomConstants.shop_0x11F,
                                     RoomConstants.shop_0x10F, RoomConstants.shop_0x110, RoomConstants.shop_0x118,
                                     RoomConstants.mini_moldorm_cave, RoomConstants.unknown_cave_bonk_cave,
                                     RoomConstants.cave_0x125, RoomConstants.hype_cave}),

    SpriteConstants.drunk_in_the_inn:           SpriteRules(npc=True, randomize=False, sub_group0=79, sub_group1=77, sub_group2=74, sub_group3=80),

    SpriteConstants.vitreous_large_eyeball:     SpriteRules(boss=True, sub_group3=61),
    SpriteConstants.vitreous_small_eyeball:     SpriteRules(boss=True, sub_group3=61),
    SpriteConstants.vitreous_lightning:         SpriteRules(boss=True, sub_group3=61),

    SpriteConstants.catfish_quake:              SpriteRules(npc=True, randomize=False, sub_group2=24),
    SpriteConstants.agahnim_teleporting_zelda_to_darkworld: SpriteRules(boss=True, sub_group0=85, sub_group1=61, sub_group2=66, sub_group3=62),
    SpriteConstants.cabbages:                   SpriteRules(never_use_overworld=True, never_use_dungeon=True, sub_group3=16),
    SpriteConstants.gibo_floating_blob:         SpriteRules(killable=True, sub_group2=40),
    SpriteConstants.thief:                      SpriteRules(cannot_have_key=True, sub_group0=(14, 21)),

    SpriteConstants.medusa:                     SpriteRules(randomize=False, is_object=True, never_use_dungeon=True, never_use_overworld=True),
    SpriteConstants.four_way_fireball_spitters: SpriteRules(randomize=False, is_object=True, never_use_overworld=True, never_use_dungeon=True),

    SpriteConstants.hokku_bokku:                SpriteRules(sub_group2=39),
    SpriteConstants.big_fairy_who_heals_you:    SpriteRules(npc=True, randomize=False, sub_group2=57, sub_group3=54),

    SpriteConstants.tektite:                    SpriteRules(killable=True, sub_group3=16),
    SpriteConstants.chain_chomp:                SpriteRules(sub_group2=39),

    SpriteConstants.trinexx:                    SpriteRules(boss=True, sub_group0=64, sub_group3=63),
    SpriteConstants.another_part_of_trinexx:    SpriteRules(boss=True, sub_group0=64, sub_group3=63),
    SpriteConstants.yet_another_party_of_trinexx:   SpriteRules(boss=True, sub_group0=64, sub_group3=63),

    SpriteConstants.blind_the_thief:            SpriteRules(boss=True, sub_group1=44, sub_group2=59),
    SpriteConstants.swamola:                    SpriteRules(is_water_sprite=True, cannot_have_key=True, sub_group3=25),
    SpriteConstants.lynel:                      SpriteRules(sub_group3=20),

    SpriteConstants.bunny_beam:                 SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.flopping_fish:              SpriteRules(never_use_dungeon=True, randomize=False)
    SpriteConstants.stal:                       SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),
    SpriteConstants.landmine:                   SpriteRules(randomize=False, never_use_overworld=True, never_use_dungeon=True, excluded_rooms=DONT_USE_IMMOVABLE_SPRITES),  # TODO

    SpriteConstants.digging_game_proprietor:    SpriteRules(npc=True, randomize=False, sub_group1=42),
    SpriteConstants.ganon:                      SpriteRules(never_use_overworld=True, never_use_dungeon=True, boss=True, sub_group0=33, sub_group1=65, sub_group2=69, sub_group3=51),
    SpriteConstants.copy_of_ganon_except_invincible:    SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False),

    SpriteConstants.heart:                      SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.green_rupee:                SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.blue_rupee:                 SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.red_rupee:                  SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.bomb_refill_1:              SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.bomb_refill_4:              SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.bomb_refill_8:              SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.small_magic_refill:         SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.full_magic_refill:          SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.arrow_refill_5:             SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.arrow_refill_10:            SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.fairy:                      SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.small_key:                  SpriteRules(never_use_overworld=True, absorbable=True, randomize=False),
    SpriteConstants.big_key:                    SpriteRules(never_use_overworld=True, never_use_dungeon=True, absorbable=True, randomize=False),

    SpriteConstants.shield_eater:               SpriteRules(never_use_dungeon=True, never_use_overworld=True, randomize=False, sub_group3=27),
    SpriteConstants.mushroom:                   SpriteRules(never_use_overworld=True, never_use_dungeon=True, randomize=False, sub_group3=17),
    SpriteConstants.fake_master_sword:          SpriteRules(sub_group3=17),
    SpriteConstants.magic_shop_dude_his_items_including_the_magic_powder:   SpriteRules(npc=True, randomize=False, sub_group0=75, sub_group3=90),

}
