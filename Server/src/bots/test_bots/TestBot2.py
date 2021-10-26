from base_bot import BaseBot
from game.player_hero import PlayerHero
from game.world import World
from framework import RADIANT_TEAM, DIRE_TEAM

party = {
    RADIANT_TEAM: [
        "npc_dota_hero_brewmaster",
        "npc_dota_hero_doom_bringer",
        "npc_dota_hero_abyssal_underlord",
        "npc_dota_hero_beastmaster",
        "npc_dota_hero_axe",
    ],
    DIRE_TEAM: [
        "npc_dota_hero_bane",
        "npc_dota_hero_batrider",
        "npc_dota_hero_dazzle",
        "npc_dota_hero_wisp",
        "npc_dota_hero_lich",
    ],
}

class TestBot2(BaseBot):
    '''
    Tests:
    - Every hero can preform action on first game_tick. ( self._world.get_game_ticks() == 1 )
    - brewmaster, doom_bringer, axe, bane and batrider should buy 1 tango stack.
    - abyssal_underlord, beastmaster, dazzle, wisp and lich should move to point 0, 0.
    '''
    
    _world: World
    _team: int
    party: list[str]
    _heroes: list[PlayerHero]

    def __init__(self, world: World, team: int) -> None:
        self._world = world
        self._team = team
        self.party = party[team]

    def initialize(self, heroes: list[PlayerHero]) -> None:
        self._heroes = heroes

    def actions(self, hero: PlayerHero) -> None:
        if self._world.get_game_ticks() == 1:
            if self._hero_name_equals_any(hero.get_name(), [
                "npc_dota_hero_brewmaster",
                "npc_dota_hero_doom_bringer",
                "npc_dota_hero_axe"
                "npc_dota_hero_bane",
                "npc_dota_hero_batrider",
            ]):
                hero.buy("item_tango")
            if self._hero_name_equals_any(hero.get_name(), [
                "npc_dota_hero_abyssal_underlord",
                "npc_dota_hero_beastmaster",
                "npc_dota_hero_dazzle",
                "npc_dota_hero_wisp",
                "npc_dota_hero_lich"
            ]):
                hero.move(0, 0, 0)

    def _hero_name_equals_any(self, to_test: str, to_test_against: list[str]) -> bool:
        for value in to_test_against:
            if to_test == value:
                return True
        return False