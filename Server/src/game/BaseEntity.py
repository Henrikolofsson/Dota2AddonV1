#!/usr/bin/env python3


from src.game.Position import Position


class BaseEntity:
    def __init__(self, data):
        self.data = data

    def setData(self, data):
        self.data = data

    def getHealth(self):
        return self.data["health"]

    def getMaxHealth(self):
        return self.data["maxHealth"]

    def getName(self):
        return self.data["name"]

    def getOrigin(self) -> Position:
        return self.data["origin"]

    def get_team(self):
        return self.data["team"]

    def getForwardVector(self):
        return self.data["forwardVector"]

    def get_id(self) -> int:
        raise NotImplemented