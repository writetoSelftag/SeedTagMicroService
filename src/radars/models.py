from django.db import models


class Radar(models.Model):
    input = models.TextField()
    response = models.TextField()


class Coordinates:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Enemy:
    type = None
    number = 0

    def __init__(self, etype, number):
        self.type = etype
        self.number = number


class Scan:
    coordinates = None
    enemies = None
    allies = 0

    def __init__(self, enemies, coordinates, allies):
        self.enemies = Enemy(enemies["type"], enemies["number"])
        self.coordinates = Coordinates(coordinates["x"], coordinates["y"])
        self.allies = allies


class RadarInput:
    protocols = []
    scan = []

    def __init__(self, protocols, scan):
        self.protocols = []
        self.scan = []
        for item in protocols:
            self.protocols.append(item)
        for item in scan:
            if "allies" not in item:
                scan = Scan(item["enemies"], item["coordinates"], 0)
            else:
                scan = Scan(item["enemies"], item["coordinates"], item["allies"])
            self.scan.append(scan)

    def get_coords(self):
        coords = self.__list_coordinates()
        if coords == "":
            return "ERROR"
        return coords

    def __list_coordinates(self):
        coordinates = None
        list_filtered = []
        for scan_item in self.scan:
            if scan_item.enemies.type == self.__avoid():
                continue
            else:
                list_filtered.append(scan_item)
                coordinates = {
                    "x": scan_item.coordinates.x,
                    "y": scan_item.coordinates.y
                }
        if len(list_filtered) == 1:
            return coordinates
        else:
            return self.__filter_coordinates_by_strategy(list_filtered)

    def __avoid(self):
        if "avoid-mech" in self.protocols:
            return "mech"
        if "prioritize-mech" in self.protocols:
            return "soldier"
        return ""

    def __filter_coordinates_by_strategy(self, scan_items):
        coordinates = None
        if "assist-allies" in self.protocols:
            only_one = []
            for scan_item in scan_items:
                if scan_item.allies > 0:
                    only_one.append(scan_item)
                    coordinates = {
                        "x": scan_item.coordinates.x,
                        "y": scan_item.coordinates.y
                    }
            if len(only_one) == 1:
                return coordinates
            else:
                scan_items = only_one

        if "avoid-crossfire" in self.protocols:
            only_one = []
            for scan_item in scan_items:
                if scan_item.allies > 0:
                    continue
                if scan_item.allies == 0:
                    only_one.append(scan_item)
                    coordinates = {
                        "x": scan_item.coordinates.x,
                        "y": scan_item.coordinates.y
                    }
            if len(only_one) == 1:
                return coordinates
            else:
                scan_items = only_one

        if "closest-enemies" in self.protocols:
            closest_coords = None
            closest_distance = 0
            for scan_item in scan_items:
                coordinates = {
                    "x": scan_item.coordinates.x,
                    "y": scan_item.coordinates.y
                }
                if closest_coords is None:
                    distance = (((scan_item.coordinates.x - 0) ** 2) + (
                            (scan_item.coordinates.y - 0) ** 2)) ** 0.5
                    if distance < 100:
                        closest_distance = distance
                        closest_coords = coordinates
                else:
                    distance = (((scan_item.coordinates.x - 0) ** 2) + ((scan_item.coordinates.y - 0) ** 2)) ** 0.5
                    if distance > 100:
                        continue
                    if distance < closest_distance:
                        closest_coords = coordinates
                        closest_distance = distance
            return closest_coords

        if "furthest-enemies" in self.protocols:
            further_coords = None
            further_distance = 0
            for scan_item in scan_items:
                coordinates = {
                    "x": scan_item.coordinates.x,
                    "y": scan_item.coordinates.y
                }
                if further_coords is None:
                    distance = (((scan_item.coordinates.x - 0) ** 2) + (
                            (scan_item.coordinates.y - 0) ** 2)) ** 0.5
                    if distance < 100:
                        further_coords = coordinates
                        further_distance = distance
                else:
                    distance = (((scan_item.coordinates.x - 0) ** 2) + ((scan_item.coordinates.y - 0) ** 2)) ** 0.5
                    if distance > 100:
                        continue
                    if distance > further_distance:
                        further_coords = coordinates
                        further_distance = distance
            return further_coords
