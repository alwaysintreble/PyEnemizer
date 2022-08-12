from enum import IntEnum

from SpriteConstants import SpriteConstants
from SpriteGroup import SpriteGroup
from Room import Room


class SpriteRequirement:
    sprite_id: int
    overlord: bool
    boss: bool
    randomize: bool = True
    killable: bool
    npc: bool
    never_use_dungeon: bool
    never_use_overworld: bool
    cannot_have_key: bool
    is_object: bool
    absorbable: bool
    is_water_sprite: bool
    is_enemy_sprite: bool = True
    group_id: list[bytes]
    sub_group0: list[bytes]
    sub_group1: list[bytes]
    sub_group2: list[bytes]
    sub_group3: list[bytes]
    parameters: bytes
    special_glitched: bool
    excluded_rooms: set[int]
    do_not_randomize_rooms: list[int]
    spawnable_rooms: list[int]

    def __init__(self, sprite_id: int = None):
        self.sprite_id = sprite_id
        self.group_id = []
        self.sub_group0 = []
        self.sub_group1 = []
        self.sub_group2 = []
        self.sub_group3 = []
        self.excluded_rooms = set()
        self.dont_randomize_rooms = []
        self.spawnable_rooms = []

    def add_group(self, group_id: list[bytes]) -> None:
        self.group_id += group_id

    def add_sub_group(self, group: int, subgroup: list[bytes]) -> None:
        if group == 0:
            self.sub_group0 += subgroup
        elif group == 1:
            self.sub_group1 += subgroup
        elif group == 2:
            self.sub_group2 += subgroup
        elif group == 3:
            self.sub_group3 += subgroup
        else:
            raise ValueError(f"{group} is not a valid value for 'group' it must be a value from 0-3")

    def sprite_in_group(self, sprite_group: SpriteGroup) -> bool:
        groups = self.group_id + self.sub_group0 + self.sub_group1 + self.sub_group2 + self.sub_group3
        return sprite_group.dungeon_group_id in groups

    def can_spawn_in_room(self, room: Room) -> bool:
        return room.room_id not in self.excluded_rooms \
               and room.room_id in self.spawnable_rooms \
               and (self.sprite_id != SpriteConstants.wallmaster or room.room_id < 256)

    def can_be_randomized_in_room(self, room: Room) -> bool:
        return self.randomize and room.room_id in self.dont_randomize_rooms


class SpriteRequirementCollection:
    requirements: list[SpriteRequirement]

    def __init__(self):
        self.requirements = []
        self.construct_requirements()

    @property
    def randomizable_sprites(self) -> list[SpriteRequirement]:
        ret = []
        for req in self.requirements:
            if req.randomize:
                ret.append(req)
        return ret

    @property
    def do_not_randomize(self) -> list[SpriteRequirement]:
        ret = []
        for req in self.requirements:
            if not req.randomize:
                ret.append(req)
        return ret

    @property
    def usable_enemy(self) -> list[SpriteRequirement]:
        ret = []
        for req in self.requirements:
            if req.is_enemy_sprite and not (req.npc or req.boss or req.overlord or req.is_object):
                ret.append(req)
        return ret

    def get_usable_dungeon_enemies(self, absorbable: bool = False) -> list[SpriteRequirement]:
        ret = []
        for req in self.usable_enemy:
            if not req.never_use_dungeon and req.absorbable == absorbable:
                ret.append(req)
        return ret

    def get_usable_overworld_enemies(self, absorbable: bool = False) -> list[SpriteRequirement]:
        ret = []
        for req in self.usable_enemy:
            if not req.never_use_overworld and req.absorbable == absorbable:
                ret.append(req)
        return ret

    @property
    def killable_sprites(self) -> list[SpriteRequirement]:
        ret = []
        for req in self.requirements:
            if req.killable:
                ret.append(req)
        return ret

    @property
    def water_sprites(self) -> list[SpriteRequirement]:
        ret = []
        for req in self.requirements:
            if req.is_water_sprite:
                ret.append(req)
        return ret

    def construct_requirements(self) -> None:
        sprite =
        self.requirements.append(SpriteRequirement(SpriteConstants.raven))
