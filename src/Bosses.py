from enum import IntEnum
from src.SpriteConstants import BOSSES


class Boss:
    rules: bool
    boss_pointer: bytearray
    boss_graphics: bytes
    boss_sprite_id: int
    requirements: str
    requirement_list: list[str]
    boss_node: str
    boss_sprite_array: bytearray


class BossGraphics(IntEnum):
    armos = 9
    lanmola = 11
    moldorm = 12
    helmasaur = 21
    arrghus = 20
    mothula = 26
    blind = 32
    kholdstare = 22
    vitreous = 22
    trinexx = 23


class ArmosBoss(Boss):
    boss_pointer: bytearray = {0x87, 0xE8}
    boss_graphics = BossGraphics.armos
    boss_sprite_id: int = BOSSES["Armos"]
    boss_node: str = "eastern-armos"

    boss_sprite_array: bytearray = {
        0x05, 0x04, 0x53,
        0x05, 0x07, 0x53,
        0x05, 0x0A, 0x53,
        0x08, 0x0A, 0x53,
        0x08, 0x07, 0x53,
        0x08, 0x04, 0x53,
        0x08, 0xE7, 0x19
    }


class LanmolaBoss(Boss):
    boss_pointer = {0xCB, 0xDC}
    boss_graphics = BossGraphics.lanmola
    boss_sprite_id = BOSSES["Lanmolas"]
    boss_node = "desert-lanmolas"

    boss_sprite_array = {
        0x07, 0x06, 0x54,
        0x07, 0x09, 0x54,
        0x09, 0x07, 0x54
    }


class MoldormBoss(Boss):
    boss_pointer = {0xC3, 0xD9}
    boss_graphics = BossGraphics.moldorm
    boss_sprite_id = BOSSES["Moldorm"]
    boss_node = "hera-moldorm"

    boss_sprite_array = {
        0x09, 0x09, 0x09
    }


class HelmasaurBoss(Boss):
    boss_pointer = {0x49, 0xE0}
    boss_graphics = BossGraphics.helmasaur
    boss_sprite_id = BOSSES["Helmasaur"]
    boss_node = "pod-helmasaur"

    boss_sprite_array = {
        0x06, 0x07, 0x92
    }


class ArrghusBoss(Boss):
    boss_pointer = {0x97, 0xD9}
    boss_graphics = BossGraphics.arrghus
    boss_sprite_id = BOSSES["Arrghus"]
    boss_node = "swamp-arrghus"

    boss_sprite_array = {
        0x07, 0x07, 0x8C,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
        0x07, 0x07, 0x8D,
    }


class MothulaBoss(Boss):
    boss_pointer = {0x31, 0xDC}
    boss_graphics = BossGraphics.mothula
    boss_sprite_id = BOSSES["Mothula"]
    boss_node = "skull-mothula"

    boss_sprite_array = {
        0x06, 0x08, 0x88  # mothula
        # 16 E7 07 # floor
    }


class BlindBoss(Boss):
    boss_pointer = {0x54, 0xE6}
    boss_graphics = BossGraphics.blind
    boss_sprite_id = BOSSES["Blind"]
    boss_node = "thieves-blind"

    boss_sprite_array = {
        0x05, 0x09, 0xCE
    }


class KholdstareBoss(Boss):
    boss_pointer = {0x01, 0xEA}
    boss_graphics = BossGraphics.kholdstare
    boss_sprite_id = BOSSES["Kholdstare"]
    boss_node = "ice-kholdstare"

    boss_sprite_array = {
        0x05, 0x07, 0xA3,  # shell
        0x05, 0x07, 0xA4,  # falling ice
        0x05, 0x07, 0xA2,  # kholdstare
    }


class VitreousBoss(Boss):
    boss_pointer = {0x57, 0xE4}
    boss_graphics = BossGraphics.vitreous
    boss_sprite_id = BOSSES["Vitreous"]
    boss_node = "mire-vitreous"

    boss_sprite_array = {
        0x05, 0x07, 0xBD
    }


class TrinexxBoss(Boss):
    boss_pointer = {0xBA, 0xE5}
    boss_graphics = BossGraphics.trinexx
    boss_sprite_id = BOSSES["Trinexx"]
    boss_node = "turtle-trinexx"

    boss_sprite_array = {
        0x05, 0x07, 0xCB,
        0x05, 0x07, 0xCC,
        0x05, 0x07, 0xCD
    }
