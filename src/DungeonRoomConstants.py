from enum import IntEnum


class BossDropItemAddress(IntEnum):
    eastern_palace = 0x180150
    desert_palace = 0x180151
    tower_of_hera = 0x180152
    palace_of_darkness = 0x180153
    swamp_palace = 0x180154
    skull_woods = 0x180155
    thieves_town = 0x180156
    ice_palace = 0x180157
    misery_mire = 0x180158
    turtle_rock = 0x180159
    ganons_tower_1 = 0x0
    ganons_tower_2 = 0x0
    ganons_tower_3 = 0x0


class RoomConstants(IntEnum):
    ganon = 0
    hyrule_castle_north_corridor = 1
    hyrule_castle_switch_room = 2
    houlihan_room = 3
    turtle_rock_crystal_roller_room = 4
    empty_clone_room_0x05 = 5
    swamp_palace_arrghus = 6
    tower_of_hera_moldorm = 7
    cave_healing_fairy = 8
    palace_of_darkness_0x09 = 9
    palace_of_darkness_stalfos_trap = 10
    palace_of_darkness_turtle_room = 11
    ganons_tower_entrance = 12
    ganons_tower_agahnim_2 = 13
    ice_palace_entrance = 14
    empty_clone_room_0x0F = 15
    ganon_evacuation_route = 16
    hyrule_castle_bombable_stock_room = 17
    sanctuary = 18
    turtle_rock_hokku_bokku_key_2 = 19
    turtle_rock_big_key = 20
    turtle_rock_0x15 = 21
    swamp_palace_swimming_treadmill = 22
    tower_of_hera_moldorm_fall = 23
    cave_0x18_big_fairy_drop_entrance = 24
    palace_of_darkness_dark_maze = 25
    palace_of_darkness_big_chest = 26
    palace_of_darkness_mimics_moving_wall = 27
    ganons_tower_ice_armos = 28
    ganons_tower_final_hallway = 29
    ice_palace_bomb_floor_bari = 30
    ice_palace_pengator_big_key = 31
    agahnims_tower_agahnim = 32
    hyrule_castle_key_rat = 33
    hyrule_castle_sewer_text_trigger = 34
    turtle_rock_west_exit = 35
    turtle_rock_double_hokku_bokku_big_chest = 36
    empty_clone_room_0x25 = 37
    swamp_palace_statue = 38
    tower_of_hera_big_chest = 39
    swamp_palace_entrance = 40
    skull_woods_mothula = 41
    palace_of_darkness_big_hub = 42
    palace_of_darkness_map_chest_fairy = 43
    cave_0x2C_hookshot_cave_backdoor = 44
    empty_clone_room_0x2D = 45
    ice_palace_compass_room = 46
    cave_kakariko_well_hp = 47
    agahnims_tower_maiden_sacrifice_chamber = 48
    tower_of_hera_hardhat_beetles = 49
    hyrule_castle_sewer_key_chest = 50
    desert_palace_lanmolas = 51
    swamp_palace_push_block_puzzle_pre_big_key = 52
    swamp_palace_big_key_bs = 53
    swamp_palace_big_chest = 54
    swamp_palace_map_chest_water_fill = 55
    swamp_palace_key_pot = 56
    skull_woods_gibdo_key_mothula_hole = 57
    palace_of_darkness_bombable_floor = 58
    palace_of_darkness_spike_block_conveyor = 59
    cave_0x3C_hookshot_cave = 60
    ganons_tower_torch_room_2 = 61
    ice_palace_stalfos_knights_conveyor_hellway = 62
    ice_palace_map_chest = 63
    agahnims_tower_final_bridge = 64
    hyrule_castle_first_dark_room = 65
    hyrule_castle_6_ropes = 66
    desert_palace_torch_puzzle_moving_wall = 67
    thieves_town_big_chest = 68
    thieves_town_jail_cells = 69
    swamp_palace_compass_chest = 70
    empty_clone_room_0x47 = 71
    empty_clone_room_0x48 = 72
    skull_woods_gibdo_torch_puzzle = 73
    palace_of_darkness_entrance = 74
    palace_of_darkness_warps_south_mimics = 75
    ganons_tower_mini_helmasaur_conveyor = 76
    ganons_tower_moldorm = 77
    ice_palace_bomb_jump = 78
    ice_palace_clone_room_fairy = 79
    hyrule_castle_west_corridor = 80
    hyrule_castle_throne = 81
    hyrule_castle_east_corridor = 82
    desert_palace_popos_2_beamos_hellway = 83
    swamp_palace_upstairs_pits = 84
    hyrule_castle_secret_entrance_uncle_death = 85
    skull_woods_key_pot_trap = 86
    skull_woods_big_key = 87
    skull_woods_big_chest = 88
    skull_woods_final_section_entrance = 89
    palace_of_darkness_helmasaur_king = 90
    ganons_tower_spike_pit_room = 91
    ganons_tower_ganon_ball_z = 92
    ganons_tower_gauntlet_1_2_3 = 93
    ice_palace_lonely_firebar = 94
    ice_palace_hidden_chest_spike_floor = 95
    hyrule_castle_west_entrance = 96
    hyrule_castle_main_entrance = 97
    hyrule_castle_east_entrance = 98
    desert_palace_final_section_entrance = 99
    thieves_town_west_attic = 100
    thieves_town_east_attic = 101
    swamp_palace_hidden_chest_hidden_door = 102
    skull_woods_compass_chest = 103
    skull_woods_key_chest_trap = 104
    empty_clone_room_0x69 = 105
    palace_of_darkness_rupees = 106
    ganons_tower_mimics = 107
    ganons_tower_lanmolas = 108
    ganons_tower_gauntlet_4_5 = 109
    ice_palace_pengators_room = 110
    empty_clone_room_0x6F = 111
    hyrule_castle_small_corridor_to_jail_cells = 112
    hyrule_castle_boomerang_chest = 113
    hyrule_castle_map_chest = 114
    desert_palace_big_chest = 115
    desert_palace_map_chest = 116
    desert_palace_big_key_chest = 117
    swamp_palace_water_drain = 118
    tower_of_hera_entrance = 119
    empty_clone_room_0x78 = 120
    empty_clone_room_0x79 = 121
    empty_clone_room_0x7A = 122
    ganons_tower = 123
    ganons_tower_east_side_collapsing_bridge = 124
    ganons_tower_winder_warp_maze = 125
    ice_palace_hidden_chest_bombable_floor = 126
    ice_palace_big_spike_traps = 127
    hyrule_castle_jail_cell = 128
    hyrule_castle_next_to_chasm = 129
    hyrule_castle_basement_chasm = 130
    desert_palace_west_entrance = 131
    desert_palace_main_entrance = 132
    desert_palace_east_entrance = 133
    empty_clone_room_0x86 = 134
    tower_of_hera_tile_room = 135
    empty_clone_room_0x88 = 136
    eastern_palace_fairy = 137
    empty_clone_room_0x8A = 138
    ganons_tower_block_puzzle_spike_skip_map_chest = 139
    ganons_tower_east_and_west_downstairs_big_chest = 140
    ganons_tower_tile_torch_puzzle = 141
    ice_palace_0x8E = 142
    empty_clone_room_0x8F = 143
    misery_mire_vitreous = 144
    misery_mire_final_switch = 145
    misery_mire_dark_bomb_wall_switches = 146
    misery_mire_dark_cane_floor_switch_puzzle = 147
    empty_clone_room_0x94 = 148
    ganons_tower_final_collapsing_bridge = 149
    ganons_tower_torches_1 = 150
    misery_mire_torch_puzzle_moving_wall = 151
    misery_mire_entrance = 152
    eastern_palace_eyegore_key = 153
    empty_clone_room_0x9A = 154
    ganons_tower_many_spikes_warp_maze = 155
    ganons_tower_invisible_floor_maze = 156
    ganons_tower_compass_chest_invisible_floor = 157
    ice_palace_big_chest = 158
    ice_palace_0x9F = 159
    misery_mire_pre_vitreous = 160
    misery_mire_fish = 161
    misery_mire_bridge_key_chest = 162
    misery_mire_0xA3 = 163
    turtle_rock_trinexx = 164
    ganons_tower_wizzrobes = 165
    ganons_tower_moldorm_fall = 166
    tower_of_hera_fairy = 167
    eastern_palace_stalfos_spawn = 168
    eastern_palace_big_chest = 169
    eastern_palace_map_chest = 170
    thieves_town_moving_spikes_key_pot = 171
    thieves_town_blind_the_thief = 172
    empty_clone_room_0xAD = 173
    ice_palace_0xAE = 174
    ice_palace_ice_bridge = 175
    agahnims_tower_circle_of_pots = 176
    misery_mire_hourglass_room = 177
    misery_mire_slug = 178
    misery_mire_spike_key_chest = 179
    turtle_rock_pre_trinexx = 180
    turtle_rock_dark_maze = 181
    turtle_rock_chain_chomps = 182
    turtle_rock_map_chest_key_chest_roller = 183
    eastern_palace_big_key = 184
    eastern_palace_lobby_cannonballs = 185
    eastern_palace_dark_antifairy_key_pot = 186
    thieves_town_hellway = 187
    thieves_town_conveyor_toilet = 188
    empty_clone_room_0xBD = 189
    ice_palace_block_puzzle = 190
    ice_palace_clone_room_switch_room = 191
    agahnims_tower_dark_bridge = 192
    misery_mire_compass_chest_tile = 193
    misery_mire_big_hub = 194
    misery_mire_big_chest = 195
    turtle_rock_final_crystal_switch_puzzle = 196
    turtle_rock_laser_bridge = 197
    turtle_rock_0xC6 = 198
    turtle_rock_torch_puzzle = 199
    eastern_palace_armos_knights = 200
    eastern_palace_entrance = 201
    unknown = 202
    thieves_town_northwest_entrance = 203
    thieves_town_northeast_entrance = 204
    empty_clone_room_0xCD = 205
    ice_palace_hole_to_kholdstare = 206
    empty_clone_room_0xCF = 207
    agahnims_tower_dark_maze = 208
    misery_mire_conveyor_slug_big_key = 209
    misery_mire_mire_02_wizzrobes = 210
    empty_clone_room_0xD3 = 211
    empty_clone_room_0xD4 = 212
    turtle_rock_laser_key = 213
    turtle_rock_entrance = 214
    empty_clone_room_0xD7 = 215
    eastern_palace_pre_armos_knights = 216
    eastern_palace_cannonball = 217
    eastern_palace = 218
    thieves_town_main_southwest_entrance = 219
    thieves_town_southeast_entrance = 220
    empty_clone_room_0xDD = 221
    ice_palace_kholdstare = 222
    cave_backwards_death_mountain_top_floor = 223
    agahnims_tower_entrance = 224
    cave_lost_woods_hp = 225
    cave_lumberjacks_tree_hp = 226
    cave_half_magic = 227
    cave_lost_old_man_final_cave = 228
    cave_lost_old_man_final_cave_2 = 229
    cave_0xE6 = 230
    cave_0xE7 = 231
    cave_0xE8 = 232
    empty_clone_room_0xE9 = 233
    cave_spectacle_rock_hp = 234
    cave_0xEB = 235
    empty_clone_room_0xEC = 236
    cave_0xED = 237
    cave_spiral_cave = 238
    cave_crystal_switch_5_chests = 239
    cave_lost_old_man_starting_cave = 240
    cave_lost_old_man_starting_cave_2 = 241
    house = 242
    house_old_woman_sahasrahlas_wife_maybe = 243
    house_angry_brothers = 244
    house_angry_brothers_2 = 245
    empty_clone_room_0xE6 = 246
    empty_clone_room_0xE7 = 247
    cave_0xF8 = 248
    cave_0xF9 = 249
    cave_0xFA = 250
    cave_0xFB = 251
    empty_clone_room_0xFC = 252
    cave_0xFD = 253
    cave_0xFE = 254
    cave_0xFF = 255
    shop_in_lost_woods_0x100 = 256
    scared_lady_houses = 257
    sick_kid = 258
    inn_bush_house = 259
    links_house = 260
    shabadoo_house = 261
    chest_game_bomb_house = 262
    library_bomb_farm = 263
    chicken_house = 264
    witch_hut = 265
    aginah = 266
    swamp_floodway = 267
    mimic_cave = 268
    cave_outside_misery_mire = 269
    cave_0x10E = 270
    shop_0x10F = 271
    shop_0x110 = 272
    archer_game = 273
    cave_shop_0x112 = 274
    kings_tomb = 275
    wishing_well_cave_0x114 = 276
    wishing_well_big_fairy = 277
    fat_fairy = 278
    spike_cave = 279
    shop_0x118 = 280
    blinds_house = 281
    mutant = 282
    mirror_cave_grove_and_tomb = 283
    bomb_shop = 284
    blinds_basement = 285
    hype_cave = 286
    shop_0x11F = 287
    ice_rod_cave = 288
    smith_house = 289
    fortune_tellers = 290
    mini_moldorm_cave = 291
    unknown_cave_bonk_cave = 292
    cave_0x125 = 293
    checker_board_cave = 294
    hammer_peg_cave = 295


NEED_KILLABLE_DOORS: set = {
    # caves
    RoomConstants.cave_crystal_switch_5_chests,  # paradox
    RoomConstants.mimic_cave,
    RoomConstants.mini_moldorm_cave,

    # hyrule castle
    RoomConstants.hyrule_castle_boomerang_chest,

    # eastern palace
    RoomConstants.eastern_palace_big_key,
    RoomConstants.eastern_palace_stalfos_spawn,
    RoomConstants.eastern_palace_pre_armos_knights,

    # desert palace
    RoomConstants.desert_palace_popos_2_beamos_hellway,
    RoomConstants.desert_palace_big_key_chest,
    RoomConstants.desert_palace_east_entrance,

    # tower of hera
    RoomConstants.tower_of_hera_hardhat_beetles,
    RoomConstants.tower_of_hera_tile_room,

    # castle tower
    RoomConstants.agahnims_tower_circle_of_pots,
    RoomConstants.agahnims_tower_dark_bridge,  # not normally required to go backwards, except in doors or glitch shenanigans
    RoomConstants.agahnims_tower_entrance,

    # palace of darkness
    RoomConstants.palace_of_darkness_turtle_room,
    RoomConstants.palace_of_darkness_mimics_moving_wall,
    RoomConstants.palace_of_darkness_warps_south_mimics,

    # swamp palace
    RoomConstants.swamp_palace_entrance,

    # thieves' town
    RoomConstants.thieves_town_big_chest,
    RoomConstants.thieves_town_jail_cells,

    # ice palace
    RoomConstants.ice_palace_entrance,
    RoomConstants.ice_palace_compass_room,
    RoomConstants.ice_palace_stalfos_knights_conveyor_hellway,
    RoomConstants.ice_palace_pengators_room,

    # misery mire
    RoomConstants.misery_mire_slug,
    RoomConstants.misery_mire_mire_02_wizzrobes,

    # turtle rock
    RoomConstants.turtle_rock_crystal_roller_room,
    RoomConstants.turtle_rock_double_hokku_bokku_big_chest,
    RoomConstants.turtle_rock_chain_chomps,

    # ganon's tower
    RoomConstants.ganons_tower_torch_room_2,
    RoomConstants.ganons_tower_gauntlet_1_2_3,
    RoomConstants.ganons_tower_mimics,
    RoomConstants.ganons_tower_gauntlet_4_5,
    RoomConstants.ganons_tower,
    RoomConstants.ganons_tower_winder_warp_maze,
    RoomConstants.ganons_tower_tile_torch_puzzle,
    RoomConstants.ganons_tower_torches_1,
    RoomConstants.ganons_tower_wizzrobes
}

# rooms with special handling

FREEZOR_ROOMS: set = {
    RoomConstants.ice_palace_entrance,
    RoomConstants.ice_palace_hidden_chest_bombable_floor,
    RoomConstants.ice_palace_0x8E,
    RoomConstants.ice_palace_big_chest,
    RoomConstants.ice_palace_block_puzzle
}
"""These rooms need to be locked on the gfx ID: 28"""


WATER_ROOMS: set = {
    RoomConstants.swamp_palace_swimming_treadmill,
    RoomConstants.swamp_palace_entrance,
    RoomConstants.swamp_palace_push_block_puzzle_pre_big_key,
    RoomConstants.swamp_palace_big_chest,
    RoomConstants.swamp_palace_key_pot,
    RoomConstants.swamp_palace_compass_chest,
    RoomConstants.swamp_palace_hidden_chest_hidden_door
}
"""These rooms need to be locked on the gfx ID: 17"""


SHADOW_ROOMS: set = {
    RoomConstants.ice_palace_stalfos_knights_conveyor_hellway,
    RoomConstants.ice_palace_0x9F
}
"""28, 27, 30"""


WALL_MASTER_ROOMS: set = {
    RoomConstants.skull_woods_gibdo_key_mothula_hole,
    RoomConstants.skull_woods_gibdo_torch_puzzle,
    RoomConstants.skull_woods_key_pot_trap,
    RoomConstants.skull_woods_key_chest_trap,
    RoomConstants.ganons_tower_tile_torch_puzzle
}
"""Force 82 on 3"""


BUMPER_AND_CRYSTAL_ROOMS: set = {
    RoomConstants.tower_of_hera_moldorm_fall,
    RoomConstants.turtle_rock_crystal_roller_room,
    RoomConstants.palace_of_darkness_turtle_room,
    RoomConstants.turtle_rock_hokku_bokku_key_2,
    RoomConstants.palace_of_darkness_mimics_moving_wall,
    RoomConstants.ice_palace_bomb_floor_bari,
    RoomConstants.palace_of_darkness_big_hub,
    RoomConstants.palace_of_darkness_map_chest_fairy,
    RoomConstants.tower_of_hera_hardhat_beetles,
    RoomConstants.thieves_town_big_chest,
    RoomConstants.ganons_tower_mini_helmasaur_conveyor,
    RoomConstants.skull_woods_big_chest,
    RoomConstants.skull_woods_final_section_entrance,
    RoomConstants.ganons_tower_spike_pit_room,
    RoomConstants.skull_woods_compass_chest,
    RoomConstants.skull_woods_key_chest_trap,
    RoomConstants.ganons_tower_mimics,
    RoomConstants.tower_of_hera_entrance,
    RoomConstants.tower_of_hera_tile_room,
    RoomConstants.ganons_tower_block_puzzle_spike_skip_map_chest,
    RoomConstants.misery_mire_final_switch,
    RoomConstants.ganons_tower_torches_1,
    RoomConstants.misery_mire_dark_bomb_wall_switches,
    RoomConstants.ganons_tower_many_spikes_warp_maze,
    RoomConstants.ganons_tower_compass_chest_invisible_floor,
    RoomConstants.misery_mire_fish,
    RoomConstants.thieves_town_moving_spikes_key_pot,
    RoomConstants.turtle_rock_chain_chomps,
    RoomConstants.ice_palace_clone_room_switch_room,
    RoomConstants.misery_mire_compass_chest_tile,
    RoomConstants.turtle_rock_final_crystal_switch_puzzle,
    RoomConstants.cave_0xEB,
    RoomConstants.agahnims_tower_final_bridge,
    RoomConstants.palace_of_darkness_entrance,
    RoomConstants.ganons_tower_wizzrobes,
    RoomConstants.misery_mire_big_chest,
    RoomConstants.turtle_rock_laser_bridge,
    RoomConstants.turtle_rock_laser_key,
    RoomConstants.turtle_rock_entrance,
    RoomConstants.cave_crystal_switch_5_chests,
    RoomConstants.ganons_tower_torch_room_2,
    RoomConstants.ice_palace_hidden_chest_bombable_floor
}
"""Also laser shooting eyes can be 82 or 83 on 3"""


SWITCHES_ROOMS: set = {
    RoomConstants.hyrule_castle_switch_room,
    RoomConstants.skull_woods_big_chest,
    RoomConstants.thieves_town_west_attic,
    RoomConstants.swamp_floodway
}


TONGUES_ROOMS: set = {
    RoomConstants.turtle_rock_crystal_roller_room,
    RoomConstants.turtle_rock_west_exit,
    RoomConstants.swamp_palace_big_key_bs,
    RoomConstants.swamp_palace_map_chest_water_fill,
    RoomConstants.ice_palace_map_chest,
    RoomConstants.swamp_palace_water_drain,
    RoomConstants.ice_palace_hole_to_kholdstare
}


NO_STATUE_ROOMS: set = {
    RoomConstants.swamp_palace_swimming_treadmill,
    RoomConstants.swamp_palace_statue,
    RoomConstants.swamp_palace_entrance,
    RoomConstants.swamp_palace_push_block_puzzle_pre_big_key,
    RoomConstants.swamp_palace_big_chest,
    RoomConstants.swamp_palace_compass_chest,
    RoomConstants.swamp_palace_water_drain,
    RoomConstants.palace_of_darkness_map_chest_fairy,
    RoomConstants.skull_woods_big_key,
    RoomConstants.misery_mire_hourglass_room,
    RoomConstants.misery_mire_big_hub,
    RoomConstants.agahnims_tower_dark_maze
}
"""Do not generate statue in these rooms"""


CANON_ROOMS: set = {
    RoomConstants.ganons_tower_ganon_ball_z,
    RoomConstants.desert_palace_big_key_chest
}


CANON_ROOMS_2: set = {
    RoomConstants.eastern_palace_lobby_cannonballs,
    RoomConstants.eastern_palace_cannonball
}


STANDARD_START_ROOMS: set = {room for room in RoomConstants if "hyrule_castle" in room.__str__()}


DONT_RANDOMIZE_ROOMS: set = {
    RoomConstants.ganon,
    RoomConstants.hyrule_castle_north_corridor,
    RoomConstants.houlihan_room,
    RoomConstants.ganons_tower_agahnim_2,
    RoomConstants.turtle_rock_big_key,
    RoomConstants.agahnims_tower_agahnim,
    RoomConstants.agahnims_tower_maiden_sacrifice_chamber,
    RoomConstants.ice_palace_big_spike_traps
}

BOSS_ROOMS: set = {
    RoomConstants.eastern_palace_armos_knights,
    RoomConstants.ganons_tower_ice_armos,
    RoomConstants.ganons_tower_lanmolas,
    RoomConstants.desert_palace_lanmolas,
    RoomConstants.tower_of_hera_moldorm,
    RoomConstants.ganons_tower_moldorm,
    RoomConstants.palace_of_darkness_helmasaur_king,
    RoomConstants.swamp_palace_arrghus,
    RoomConstants.skull_woods_mothula,
    RoomConstants.thieves_town_blind_the_thief,
    RoomConstants.ice_palace_kholdstare,
    RoomConstants.misery_mire_vitreous,
    RoomConstants.turtle_rock_trinexx,
    RoomConstants.agahnims_tower_agahnim,
    RoomConstants.ganons_tower_agahnim_2,
    RoomConstants.ganon
}
