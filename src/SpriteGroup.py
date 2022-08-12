class SpriteGroup:
    sprite_group_base_address: int = 0x5B97
    group_id: int
    dungeon_group_id: int
    sub_group0: int
    sub_group1: int
    sub_group2: int
    sub_group3: int
    preserve_sub_group0: bool
    preserve_sub_group1: bool
    preserve_sub_group2: bool
    preserve_sub_group3: bool
    force_rooms_to_group: list[int]


