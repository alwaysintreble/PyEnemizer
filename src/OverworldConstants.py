from enum import IntEnum


class OverworldConstants(IntEnum):
    # light world
    lost_woods = 0x000
    lost_woods_2 = 0x001
    lumber_jack_house = 0x002
    west_death_mountain = 0x003
    west_death_mountain_2 = 0x004
    east_death_mountain = 0x005
    east_death_mountain_2 = 0x006
    east_death_mountain_warp_for_turtle_rock = 0x007
    lost_woods_3 = 0x008
    lost_woods_4 = 0x009
    entrance_to_death_mountain = 0x00A
    west_death_mountain_3 = 0x00B
    west_death_mountain_4 = 0x00C
    east_death_mountain_3 = 0x00D
    east_death_mountain_3_2 = 0x00E
    entrance_to_zoras_domain = 0x00F
    path_between_kakariko_and_lost_woods = 0x010
    kakariko_fortune_teller = 0x011
    pond_near_fortune_teller = 0x012
    sanctuary = 0x013
    graveyard = 0x014
    river_between_graveyard_and_witch = 0x015
    witch_hut = 0x016
    east_of_witch_hut = 0x017
    kakariko_village = 0x018
    kakariko_village_2 = 0x019
    forest_between_kakariko_and_hyrule_castle = 0x01A
    hyrule_castle = 0x01B
    hyrule_castle_2 = 0x01C
    bridge_between_graveyard_and_witch_hut = 0x01D
    eastern_palace = 0x01E
    eastern_palace_2 = 0x01F
    kakariko_village_3 = 0x020
    kakariko_village_4 = 0x021
    smithy = 0x022
    hyrule_castle_3 = 0x023
    hyrule_castle_4 = 0x024
    path_between_hyrule_castle_and_eastern_palace_top = 0x025
    eastern_palace_3 = 0x026
    eastern_palace_4 = 0x027
    kakariko_village_maze_raze = 0x028
    kakariko_village_library = 0x029
    haunted_grove = 0x02A
    forest_between_haunted_grove_and_links_house = 0x02B
    links_house = 0x02C
    path_between_hyrule_castle_and_eastern_palace_bottom = 0x02D
    caves_south_of_eastern_palace_left = 0x02E
    caves_south_of_eastern_palace_right = 0x02F
    desert_of_mystery = 0x030
    desert_of_mystery_2 = 0x031
    south_of_haunted_grove = 0x032
    northwestern_great_swamp = 0x033
    northeastern_great_swamp = 0x034
    lake_hylia = 0x035
    lake_hylia_2 = 0x036
    ice_cave = 0x037
    desert_of_mystery_3 = 0x038
    desert_of_mystery_4 = 0x039
    path_between_desert_of_mystery_and_great_swamp = 0x03A
    southwestern_great_swamp = 0x03B
    southeastern_great_swamp = 0x03C
    lake_hylia_3 = 0x03D
    lake_hylia_4 = 0x03E
    path_between_lake_hylia_and_ice_cave = 0x03F

    # dark world
    skull_woods = 0x040
    lumber_jack_house_wrong_dw = 0x041
    lumber_jack_house_dw = 0x042
    west_death_mountain_dw = 0x043
    east_death_mountain_wrong_dw = 0x044
    east_death_mountain_dw = 0x045
    unknown_should_be_east_fake = 0x046
    turtle_rock = 0x047
    lost_woods_3_dw = 0x048
    lost_woods_4_dw = 0x049
    bumper_cave_entrance_dw = 0x04A
    west_death_mountain_3_dw = 0x04B
    west_death_mountain_4_dw = 0x04C
    east_death_mountain_3_dw = 0x04D
    east_death_mountain_4_dw = 0x04E
    catfish = 0x04F
    path_between_village_of_outcasts_and_skull_woods = 0x050
    village_of_outcasts_fortune_teller = 0x051
    pond_between_village_of_outcasts_fortune_teller_and_sanc = 0x052
    sanctuary_dw = 0x053
    graveyard_dw = 0x054
    river_between_graveyard_and_witch_dw = 0x055
    witch_hut_dw = 0x056
    east_of_witch_hut_dw = 0x057
    village_of_outcasts = 0x058
    village_of_outcasts_2 = 0x059
    forest_between_village_of_outcasts_and_pyramid = 0x05A
    pyramid = 0x05B
    pyramid_2 = 0x05C
    broken_bridge_between_graveyard_and_witch_hut_dw = 0x05D
    palace_of_darkness = 0x05E
    palace_of_darkness_2 = 0x05F
    village_of_outcasts_3 = 0x060
    village_of_outcasts_4 = 0x061
    smith_dw = 0x062
    pyramid_3 = 0x063
    pyramid_4 = 0x064
    path_between_pyramid_and_palace_of_darkness_top = 0x065
    palace_of_darkness_3 = 0x066
    palace_of_darkness_4 = 0x067
    digging_game = 0x068
    village_of_outcasts_frog_smith = 0x069
    haunted_grove_dw = 0x06A
    forest_between_haunted_grove_and_links_house_dw = 0x06B
    bomb_shop_links_house = 0x06C
    path_between_pyramid_and_palace_of_darkness_bottom = 0x06B
    caves_south_of_palace_of_darkness_left = 0x06E
    caves_south_of_palace_of_darkness_right = 0x06F
    misery_mire = 0x070
    south_of_haunted_grove_fake_dw = 0x071
    south_of_haunted_grove_dw = 0x072
    northwestern_great_swamp_dw = 0x073
    northeastern_great_swamp_dw = 0x074
    lake_hylia_dw = 0x075
    ice_cave_fake_dw = 0x076
    ice_cave_dw = 0x077
    misery_mire_3 = 0x078
    misery_mire_4 = 0x079
    path_between_misery_mire_and_great_swamp = 0x07A
    southwestern_great_swamp_dw = 0x07B
    southeastern_great_swamp_dw = 0x07C
    lake_hylia_3_dw = 0x07D
    lake_hylia_4_dw = 0x07E
    path_between_lake_hylia_and_ice_cave_dw = 0x07F

    master_sword_glade_under_bridge = 0x080
    zoras_domain = 0x081

    unknown_0x82 = 0x082
    unknown_0x83 = 0x083
    unknown_0x84 = 0x084
    unknown_0x85 = 0x085
    unknown_0x86 = 0x086
    unknown_0x87 = 0x087
    unknown_0x88 = 0x088
    unknown_0x89 = 0x089
    unknown_0x8A = 0x08A
    unknown_0x8B = 0x08B
    unknown_0x8C = 0x08C
    unknown_0x8D = 0x08D
    unknown_0x8E = 0x08E
    unknown_0x8F = 0x08F

    # post aga

    # light world post aga
    lost_woods_post_aga = 0x090
    lost_woods_2_post_aga = 0x091
    lumber_jack_house_post_aga = 0x092
    west_death_mountain_post_aga = 0x093
    west_death_mountain_2_post_aga = 0x094
    east_death_mountain_post_aga = 0x095
    east_death_mountain_2_post_aga = 0x096
    east_death_mountain_warp_for_turtle_rock_post_aga = 0x097
    lost_woods_3_post_aga = 0x098
    lost_woods_4_post_aga = 0x099
    entrance_to_death_mountain_post_aga = 0x09A
    west_death_mountain_3_post_aga = 0x09B
    west_death_mountain_4_post_aga = 0x09C
    east_death_mountain_3_post_aga = 0x09D
    east_death_mountain_3_2_post_aga = 0x09E
    entrance_to_zoras_domain_post_aga = 0x09F
    path_between_kakariko_and_lost_woods_post_aga = 0x0A0
    kakariko_fortune_teller_post_aga = 0x0A1
    pond_near_fortune_teller_post_aga = 0x0A2
    sanctuary_post_aga = 0x0A3
    graveyard_post_aga = 0x0A4
    river_between_graveyard_and_witch_post_aga = 0x0A5
    witch_hut_post_aga = 0x0A6
    east_of_witch_hut_post_aga = 0x0A7
    kakariko_village_post_aga = 0x0A8
    kakariko_village_2_post_aga = 0x0A9
    forest_between_kakariko_and_hyrule_castle_post_aga = 0x0AA
    hyrule_castle_post_aga = 0x0AB
    hyrule_castle_2_post_aga = 0x0AC
    bridge_between_graveyard_and_witch_hut_post_aga = 0x0AD
    eastern_palace_post_aga = 0x0AE
    eastern_palace_2_post_aga = 0x0AF
    kakariko_village_3_post_aga = 0x0B0
    kakariko_village_4_post_aga = 0x0B1
    smithy_post_aga = 0x0B2
    hyrule_castle_3_post_aga = 0x0B3
    hyrule_castle_4_post_aga = 0x0B4
    path_between_hyrule_castle_and_eastern_palace_top_post_aga = 0x0B5
    eastern_palace_3_post_aga = 0x0B6
    eastern_palace_4_post_aga = 0x0B7
    kakariko_village_maze_raze_post_aga = 0x0B8
    kakariko_village_library_post_aga = 0x0B9
    haunted_grove_post_aga = 0x0BA
    forest_between_haunted_grove_and_links_house_post_aga = 0x0BB
    links_house_post_aga = 0x0BC
    path_between_hyrule_castle_and_eastern_palace_bottom_post_aga = 0x0BD
    caves_south_of_eastern_palace_left_post_aga = 0x0BE
    caves_south_of_eastern_palace_right_post_aga = 0x0BF
    desert_of_mystery_post_aga = 0x0C0
    desert_of_mystery_2_post_aga = 0x0C1
    south_of_haunted_grove_post_aga = 0x0C2
    northwestern_great_swamp_post_aga = 0x0C3
    northeastern_great_swamp_post_aga = 0x0C4
    lake_hylia_post_aga = 0x0C5
    lake_hylia_2_post_aga = 0x0C6
    ice_cave_post_aga = 0x0C7
    desert_of_mystery_3_post_aga = 0x0C8
    desert_of_mystery_4_post_aga = 0x0C9
    path_between_desert_of_mystery_and_great_swamp_post_aga = 0x0CA
    southwestern_great_swamp_post_aga = 0x0CB
    southeastern_great_swamp_post_aga = 0x0CC
    lake_hylia_3_post_aga = 0x0CD
    lake_hylia_4_post_aga = 0x0CE
    path_between_lake_hylia_and_ice_cave_post_aga = 0x0CF

    # dark world (post aga)
    skull_woods_post_aga = 0x0D0
    lumber_jack_house_dw_post_aga = 0x0D1
    lumber_jack_house_wrong_dw_post_aga = 0x0D2
    west_death_mountain_dw_post_aga = 0x0D3
    east_death_mountain_dw_post_aga = 0x0D4
    east_death_mountain_2_dw_post_aga = 0x0D5
    unknown_0xD6 = 0x0D6
    turtle_rock_post_aga = 0x0D7
    lost_woods_3_dw_post_aga = 0x0D8
    lost_woods_4_dw_post_aga = 0x0D9
    bumper_cave_entrance_dw_post_aga = 0x0DA
    west_death_mountain_3_dw_post_aga = 0x0DB
    west_death_mountain_4_dw_post_aga = 0x0DC
    east_death_mountain_3_dw_post_aga = 0x0DD
    east_death_mountain_4_dw_post_aga = 0x0DE
    catfish_post_aga = 0x0DF
    path_between_village_of_outcasts_and_skull_woods_post_aga = 0x0E0
    village_of_outcasts_fortune_teller_post_aga = 0x0E1
    pond_between_village_of_outcasts_fortune_teller_and_sanc_post_aga = 0x0E2
    sanctuary_dw_post_aga = 0x0E3
    graveyard_dw_post_aga = 0x0E4
    river_between_graveyard_and_witch_dw_post_aga = 0x0E5
    witch_hut_dw_post_aga = 0x0E6
    east_of_witch_hut_dw_post_aga = 0x0E7
    village_of_outcasts_post_aga = 0x0E8
    village_of_outcasts_2_post_aga = 0x0E9
    forest_between_village_of_outcasts_and_pyramid_post_aga = 0x0EA
    pyramid_post_aga = 0x0EB
    pyramid_2_post_aga = 0x0EC
    broken_bridge_between_graveyard_and_witch_hut_dw_post_aga = 0x0ED
    palace_of_darkness_post_aga = 0x0EE
    palace_of_darkness_2_post_aga = 0x0EF
    village_of_outcasts_3_post_aga = 0x0F0
    village_of_outcasts_4_post_aga = 0x0F1
    smithy_dw_post_aga = 0x0F3
    pyramid_3_post_aga = 0x0F4
    path_between_pyramid_and_palace_of_darkness_top_post_aga = 0x0F5
    palace_of_darkness_3_post_aga = 0x0F6
    palace_of_darkness_4_post_aga = 0x0F7
    digging_game_post_aga = 0x0F8
    village_of_outcasts_frog_smith_post_aga = 0x0F9
    haunted_grove_dw_post_aga = 0x0FA
    forest_between_haunted_grove_and_links_house_dw_post_aga = 0x0FB
    bomb_shop_links_house_post_aga = 0x0FC
    path_between_pyramid_and_palace_of_darkness_bottom_post_aga = 0x0FD
    caves_south_of_palace_of_darkness_left_post_aga = 0x0FE
    caves_south_of_palace_of_darkness_right_post_aga = 0x0FF
    misery_mire_post_aga = 0x100
    south_of_haunted_grove_dw_post_aga = 0x101
    south_of_haunted_grove_fake_dw_post_aga = 0x102
    northwestern_great_swamp_dw_post_aga = 0x103
    northeastern_great_swamp_dw_post_aga = 0x104
    lake_hylia_dw_post_aga = 0x105
    ice_cave_dw_post_aga = 0x106
    ice_cave_fake_dw_post_aga = 0x107
    misery_mire_3_post_aga = 0x108
    misery_mire_4_post_aga = 0x109
    path_between_misery_mire_and_great_swamp_post_aga = 0x10A
    southwestern_great_swamp_dw_post_aga = 0x10B
    southeastern_great_swamp_dw_post_aga = 0x10C
    lake_hylia_3_dw_post_aga = 0x10D
    lake_hylia_4_dw_post_aga = 0x10E
    path_between_lake_hylia_and_ice_cave_dw_post_aga = 0x10F

    master_sword_glade_under_bridge_post_aga = 0x110
    zoras_domain_post_aga = 0x111


DO_NOT_RANDOMIZE_AREAS: set = {
    OverworldConstants.lost_woods_2,
    OverworldConstants.west_death_mountain_2,
    OverworldConstants.east_death_mountain_2,
    OverworldConstants.lost_woods_3,
    OverworldConstants.lost_woods_4,
    OverworldConstants.west_death_mountain_3,
    OverworldConstants.west_death_mountain_4,
    OverworldConstants.east_death_mountain_3,
    OverworldConstants.east_death_mountain_3_2,
    OverworldConstants.kakariko_village_2,
    OverworldConstants.hyrule_castle_2,
    OverworldConstants.eastern_palace_2,
    OverworldConstants.kakariko_village_3,
    OverworldConstants.eastern_palace_4,
    OverworldConstants.desert_of_mystery_2,
    OverworldConstants.lake_hylia_2,
    OverworldConstants.desert_of_mystery_3,
    OverworldConstants.desert_of_mystery_4,
    OverworldConstants.lake_hylia_3,
    OverworldConstants.lake_hylia_4,
    OverworldConstants.lumber_jack_house_wrong_dw,
    OverworldConstants.east_death_mountain_wrong_dw,
    OverworldConstants.unknown_should_be_east_fake,
    OverworldConstants.lost_woods_3_dw,
    OverworldConstants.lost_woods_4_dw,
    OverworldConstants.west_death_mountain_3_dw,
    OverworldConstants.west_death_mountain_4_dw,
    OverworldConstants.east_death_mountain_3_dw,
    OverworldConstants.east_death_mountain_4_dw,
    OverworldConstants.village_of_outcasts_2,
    OverworldConstants.pyramid_2,
    OverworldConstants.palace_of_darkness_2,
    OverworldConstants.village_of_outcasts_3,
    OverworldConstants.village_of_outcasts_4,
    OverworldConstants.pyramid_3,
    OverworldConstants.pyramid_4,
    OverworldConstants.palace_of_darkness_3,
    OverworldConstants.palace_of_darkness_4,
    OverworldConstants.south_of_haunted_grove_fake_dw,
    OverworldConstants.ice_cave_fake_dw,
    OverworldConstants.misery_mire_3,
    OverworldConstants.misery_mire_4,
    OverworldConstants.lake_hylia_3,
    OverworldConstants.lake_hylia_4,
    OverworldConstants.haunted_grove,
    OverworldConstants.haunted_grove_dw,

    OverworldConstants.unknown_0x82,
    OverworldConstants.unknown_0x83,
    OverworldConstants.unknown_0x84,
    OverworldConstants.unknown_0x85,
    OverworldConstants.unknown_0x86,
    OverworldConstants.unknown_0x87,
    OverworldConstants.unknown_0x88,
    OverworldConstants.unknown_0x89,
    OverworldConstants.unknown_0x8A,
    OverworldConstants.unknown_0x8B,
    OverworldConstants.unknown_0x8C,
    OverworldConstants.unknown_0x8D,
    OverworldConstants.unknown_0x8E,
    OverworldConstants.unknown_0x8F,

    OverworldConstants.haunted_grove_post_aga,
    OverworldConstants.haunted_grove_dw_post_aga,

    OverworldConstants.lost_woods_2_post_aga,
    OverworldConstants.west_death_mountain_2_post_aga,
    OverworldConstants.east_death_mountain_2_post_aga,
    OverworldConstants.lost_woods_3_post_aga,
    OverworldConstants.lost_woods_4_post_aga,
    OverworldConstants.west_death_mountain_3_post_aga,
    OverworldConstants.west_death_mountain_4_post_aga,
    OverworldConstants.east_death_mountain_3_2_post_aga,
    OverworldConstants.kakariko_village_2_post_aga,
    OverworldConstants.hyrule_castle_2_post_aga,
    OverworldConstants.east_death_mountain_2_post_aga,
    OverworldConstants.kakariko_village_3_post_aga,
    OverworldConstants.kakariko_village_4_post_aga,
    OverworldConstants.hyrule_castle_3_post_aga,
    OverworldConstants.hyrule_castle_4_post_aga,
    OverworldConstants.eastern_palace_3_post_aga,
    OverworldConstants.eastern_palace_4_post_aga,
    OverworldConstants.desert_of_mystery_2_post_aga,
    OverworldConstants.lake_hylia_2_post_aga,
    OverworldConstants.desert_of_mystery_3_post_aga,
    0x112,
    0x113,
    0x114,
    0x115,
    0x116,
    0x117,
    0x119,
    0x120
}
