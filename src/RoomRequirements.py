from DungeonRoomConstants import RoomConstants


class RoomGroupRequirement:
    rooms: list[int]
    group_id: int
    sub_group0: int
    sub_group1: int
    sub_group2: int
    sub_group3: int

    def __init__(self, group_id: int = None, sub_group0: int = None, sub_group1: int = None, sub_group2: int = None,
                 sub_group3: int = None, rooms: list[int] = []):
        if not (group_id or sub_group0 or sub_group1 or sub_group2 or sub_group3):
            raise ValueError("RoomGroupRequirement needs at least one non-null group id or sub group")
        self.group_id = group_id
        self.sub_group0 = sub_group0
        self.sub_group1 = sub_group1
        self.sub_group2 = sub_group2
        self.sub_group3 = sub_group3
        self.rooms = rooms


class RoomGroupRequirementCollection:
    room_requirements: list[RoomGroupRequirement]

    def __init__(self):
        self.room_requirements = []
        self.fill_room_requirements()

    def get_group_requirement_for_room(self, room: Room) -> SpriteRequirement:
        ret = SpriteRequirement(0)
        for req in self.room_requirements:
            if room in req:
                if not req.group_id:

                if not req.sub_group0:

                if not req.sub_group1:

                if not req.sub_group2:

                if not req.sub_group3:
        return ret

    def fill_room_requirements(self) -> None:
        self.room_requirements.append(
            RoomGroupRequirement(1, 70, 73, 28, 82, [
                RoomConstants.cave_lost_old_man_final_cave,
                RoomConstants.cave_lost_old_man_starting_cave
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(5, 75, 77, 74, 90, [
                RoomConstants.house_old_woman_sahasrahlas_wife_maybe,
                RoomConstants.witch_hut,
                RoomConstants.cave_0x10E,
                RoomConstants.shop_0x10F,
                RoomConstants.shop_0x110,
                RoomConstants.archer_game,
                RoomConstants.mutant,
                RoomConstants.bomb_shop,
                RoomConstants.fortune_tellers
            ])
        )
        # TODO can probably be combined with above. needs testing
        self.room_requirements.append(
            RoomGroupRequirement(sub_group0=75, rooms=[
                RoomConstants.cave_0xFF,
                RoomConstants.cave_shop_0x112,
                RoomConstants.shop_0x11F
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group1=77, sub_group3=21, rooms=[
                RoomConstants.smith_house
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(7, 75, 77, 57, 54, [
                RoomConstants.cave_healing_fairy,
                RoomConstants.cave_0x2C_hookshot_cave_backdoor,
                RoomConstants.wishing_well_cave_0x114,
                RoomConstants.wishing_well_big_fairy
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(13, 81, rooms=[
                RoomConstants.hyrule_castle_secret_entrance_uncle_death,
                RoomConstants.sick_kid,
                RoomConstants.links_house
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(14, 71, 73, 76, 80, [
                RoomConstants.sanctuary,
                RoomConstants.shabadoo_house,
                RoomConstants.aginah
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=80, rooms=[
                RoomConstants.chicken_house
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(15, 79, 77, 74, 80, [
                RoomConstants.house_angry_brothers,
                RoomConstants.house_angry_brothers_2,
                RoomConstants.scared_lady_houses,
                RoomConstants.inn_bush_house,
                RoomConstants.chest_game_bomb_house,
                RoomConstants.shop_0x118,
                RoomConstants.blinds_house
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(18, 85, 61, 66, 67, [
                RoomConstants.agahnims_tower_agahnim,
                RoomConstants.agahnims_tower_maiden_sacrifice_chamber
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(24, 85, 26, 66, 67, [
                RoomConstants.ganons_tower_agahnim_2
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(34, 33, 65, 69, 51, [
                RoomConstants.ganon
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(40, 14, None, 74, 80, [
                RoomConstants.cave_lost_woods_hp,
                RoomConstants.shop_in_lost_woods_0x100,
                RoomConstants.cave_0x125,
                RoomConstants.unknown_cave_bonk_cave,
                RoomConstants.checker_board_cave
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group0=14, sub_group1=30, rooms=[
                RoomConstants.mini_moldorm_cave
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(9, sub_group3=29, rooms=[
                RoomConstants.cave_half_magic
            ])
        )

        # freezor rooms
        self.room_requirements.append(
            RoomGroupRequirement(28, sub_group2=38, sub_group3=82, rooms=[
                RoomConstants.ice_palace_entrance,
                RoomConstants.ice_palace_hidden_chest_bombable_floor,
                RoomConstants.ice_palace_0x8E,
                RoomConstants.ice_palace_big_chest,
                RoomConstants.ice_palace_block_puzzle
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(3, 93, rooms=[
                RoomConstants.hyrule_castle_throne
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(42, 21, rooms=[
                RoomConstants.hype_cave
            ])
        )

        # cannonball shooters
        self.room_requirements.append(
            RoomGroupRequirement(10, 47, None, 46, None, [
                RoomConstants.ganons_tower_ganon_ball_z,
                RoomConstants.desert_palace_big_key_chest,
                RoomConstants.eastern_palace_lobby_cannonballs,
                RoomConstants.eastern_palace_cannonball
            ])
        )

        # pirogusu
        self.room_requirements.append(
            RoomGroupRequirement(sub_group2=34, rooms=[
                RoomConstants.swamp_palace_big_chest,
                RoomConstants.swamp_palace_compass_chest,
                RoomConstants.swamp_palace_hidden_chest_hidden_door,
                RoomConstants.swamp_palace_water_drain
            ])
        )

        # babasu
        self.room_requirements.append(
            RoomGroupRequirement(sub_group1=32, rooms=[
                RoomConstants.ice_palace_stalfos_knights_conveyor_hellway,
                RoomConstants.ice_palace_0x9F
            ])
        )

        # bari
        self.room_requirements.append(
            RoomGroupRequirement(sub_group0=31, rooms=[
                RoomConstants.ice_palace_big_spike_traps
            ])
        )

        # wallmaster
        self.room_requirements.append(
            RoomGroupRequirement(sub_group2=35, rooms=[
                RoomConstants.skull_woods_gibdo_key_mothula_hole,
                RoomConstants.skull_woods_gibdo_torch_puzzle,
                RoomConstants.skull_woods_key_pot_trap,
                RoomConstants.skull_woods_big_key,
                RoomConstants.skull_woods_key_chest_trap,
                RoomConstants.ganons_tower_tile_torch_puzzle
            ])
        )

        # guruguru bar - 31
        # cane platform - 39
        self.room_requirements.append(
            RoomGroupRequirement(37, 31, None, 39, 82, [
                RoomConstants.turtle_rock_double_hokku_bokku_big_chest,
                RoomConstants.turtle_rock_pre_trinexx,
                RoomConstants.turtle_rock_dark_maze,
                RoomConstants.turtle_rock_0xC6,
                RoomConstants.turtle_rock_torch_puzzle,
                RoomConstants.turtle_rock_entrance
            ])
        )

        # bumpers
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.tower_of_hera_moldorm_fall,
                RoomConstants.palace_of_darkness_big_hub,
                RoomConstants.thieves_town_big_chest,
                RoomConstants.ganons_tower_mini_helmasaur_conveyor,
                RoomConstants.skull_woods_key_pot_trap,
                RoomConstants.skull_woods_big_chest,
                RoomConstants.skull_woods_final_section_entrance,
                RoomConstants.skull_woods_compass_chest,
                RoomConstants.skull_woods_key_chest_trap,
                RoomConstants.ice_palace_hidden_chest_bombable_floor,
                RoomConstants.ganons_tower_block_puzzle_spike_skip_map_chest,
                RoomConstants.cave_0xEB,
                RoomConstants.cave_0xFB
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.tower_of_hera_moldorm_fall,
                RoomConstants.palace_of_darkness_big_hub,
                RoomConstants.ganons_tower_mini_helmasaur_conveyor,
                RoomConstants.skull_woods_final_section_entrance,
                RoomConstants.skull_woods_compass_chest,
                RoomConstants.skull_woods_key_chest_trap,
                RoomConstants.ice_palace_hidden_chest_bombable_floor,
                RoomConstants.ganons_tower_block_puzzle_spike_skip_map_chest,
                RoomConstants.cave_0xEB,
                RoomConstants.cave_0xFB
            ])
        )

        # crystal switches
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.palace_of_darkness_turtle_room,
                RoomConstants.turtle_rock_hokku_bokku_key_2,
                RoomConstants.palace_of_darkness_mimics_moving_wall,
                RoomConstants.ice_palace_bomb_floor_bari,
                RoomConstants.palace_of_darkness_big_hub,
                RoomConstants.palace_of_darkness_map_chest_fairy,
                RoomConstants.tower_of_hera_hardhat_beetles,
                RoomConstants.ganons_tower_torch_room_2,
                RoomConstants.ice_palace_stalfos_knights_conveyor_hellway,
                RoomConstants.ganons_tower_spike_pit_room,
                RoomConstants.ganons_tower_mimics,
                RoomConstants.tower_of_hera_entrance,
                RoomConstants.tower_of_hera_tile_room,
                RoomConstants.ganons_tower_block_puzzle_spike_skip_map_chest,
                RoomConstants.misery_mire_final_switch,
                RoomConstants.misery_mire_dark_bomb_wall_switches,
                RoomConstants.ganons_tower_many_spikes_warp_maze,
                RoomConstants.ganons_tower_compass_chest_invisible_floor,
                RoomConstants.misery_mire_fish,
                RoomConstants.thieves_town_moving_spikes_key_pot,
                RoomConstants.turtle_rock_chain_chomps,
                RoomConstants.ice_palace_clone_room_switch_room,
                RoomConstants.misery_mire_compass_chest_tile,
                RoomConstants.turtle_rock_final_crystal_switch_puzzle,
                RoomConstants.cave_crystal_switch_5_chests
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.palace_of_darkness_turtle_room,
                RoomConstants.turtle_rock_hokku_bokku_key_2,
                RoomConstants.palace_of_darkness_mimics_moving_wall,
                RoomConstants.ice_palace_bomb_floor_bari,
                RoomConstants.palace_of_darkness_big_hub,
                RoomConstants.palace_of_darkness_map_chest_fairy,
                RoomConstants.tower_of_hera_hardhat_beetles,
                RoomConstants.swamp_palace_big_key_bs,
                RoomConstants.ice_palace_stalfos_knights_conveyor_hellway,
                RoomConstants.ganons_tower_spike_pit_room,
                RoomConstants.ganons_tower_mimics,
                RoomConstants.tower_of_hera_entrance,
                RoomConstants.tower_of_hera_tile_room,
                RoomConstants.ganons_tower_block_puzzle_spike_skip_map_chest,
                RoomConstants.misery_mire_final_switch,
                RoomConstants.misery_mire_dark_bomb_wall_switches,
                RoomConstants.ganons_tower_many_spikes_warp_maze,
                RoomConstants.ganons_tower_compass_chest_invisible_floor,
                RoomConstants.misery_mire_fish,
                RoomConstants.thieves_town_moving_spikes_key_pot,
                RoomConstants.turtle_rock_chain_chomps,
                RoomConstants.ice_palace_clone_room_switch_room,
                RoomConstants.misery_mire_compass_chest_tile,
                RoomConstants.turtle_rock_final_crystal_switch_puzzle,
                RoomConstants.cave_crystal_switch_5_chests
            ])
        )

        # laser eyes
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.turtle_rock_hokku_bokku_key_2,
                RoomConstants.turtle_rock_west_exit,
                RoomConstants.ganons_tower_torches_1,
                RoomConstants.ganons_tower_wizzrobes,
                RoomConstants.misery_mire_big_chest,
                RoomConstants.turtle_rock_laser_bridge,
                RoomConstants.turtle_rock_laser_key
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.turtle_rock_hokku_bokku_key_2,
                RoomConstants.turtle_rock_west_exit,
                RoomConstants.ganons_tower_torches_1,
                RoomConstants.ganons_tower_wizzrobes,
                RoomConstants.turtle_rock_laser_bridge,
                RoomConstants.turtle_rock_laser_key
            ])
        )

        # statues
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.palace_of_darkness_big_chest,
                RoomConstants.swamp_palace_statue,
                RoomConstants.palace_of_darkness_map_chest_fairy,
                RoomConstants.agahnims_tower_final_bridge,
                RoomConstants.palace_of_darkness_entrance,
                RoomConstants.skull_woods_big_key,
                RoomConstants.ganons_tower_mimics,
                RoomConstants.ganons_tower
            ])
        )

        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.swamp_palace_statue,
                RoomConstants.palace_of_darkness_map_chest_fairy,
                RoomConstants.agahnims_tower_final_bridge,
                RoomConstants.palace_of_darkness_entrance,
                RoomConstants.skull_woods_big_key,
                RoomConstants.ganons_tower_mimics,
                RoomConstants.ganons_tower,
                RoomConstants.ice_palace_hole_to_kholdstare
            ])
        )

        # pull switch (handle)
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.hyrule_castle_switch_room,
                RoomConstants.skull_woods_big_chest,
                RoomConstants.thieves_town_west_attic,
                RoomConstants.ganons_tower_east_and_west_downstairs_big_chest,
                RoomConstants.swamp_floodway
            ])
        )

        # floor drop
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=82, rooms=[
                RoomConstants.palace_of_darkness_big_chest,
                RoomConstants.ganons_tower_torch_room_2,
                RoomConstants.thieves_town_big_chest,
                RoomConstants.skull_woods_key_pot_trap,
                RoomConstants.ice_palace_lonely_firebar,
                RoomConstants.ganons_tower_east_side_collapsing_bridge,
                RoomConstants.ganons_tower_final_collapsing_bridge,
                RoomConstants.misery_mire_big_chest
            ])
        )

        # pull switch (tongue)
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.turtle_rock_crystal_roller_room,
                RoomConstants.ice_palace_map_chest,
                RoomConstants.ice_palace_hole_to_kholdstare
            ])
        )

        # push switch (swamp)
        self.room_requirements.append(
            RoomGroupRequirement(sub_group3=83, rooms=[
                RoomConstants.swamp_palace_big_key_bs,
                RoomConstants.swamp_palace_map_chest_water_fill,
                RoomConstants.swamp_palace_water_drain
            ])
        )

        # force water tektite
        self.room_requirements.append(
            RoomGroupRequirement(sub_group2=34, rooms=[
                RoomConstants.swamp_palace_entrance
            ])
        )

        # force wizzrobe
        self.room_requirements.append(
            RoomGroupRequirement(sub_group2=37, rooms=[
                RoomConstants.misery_mire_torch_puzzle_moving_wall
            ])
        )
