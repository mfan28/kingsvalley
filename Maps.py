import os
from GlobalVar import *


class Maps:
    countMaps = 0
    curMap = 1
    maps = []

    def __init__(self):
        self.path = path_abs + "/map"
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                self.countMaps += 1
                self.load_map(filename)
                print(filename)

    def load_map(self, filename):
        fullfilename = self.path + "/" + filename
        with open(fullfilename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
            self.maps.append([filename, level_map])

            max_width = max(map(len, level_map))

    def get_map(self, nummap):
        return self.maps[nummap - 1]

    def get_nextmap(self):
        self.curMap += 1
        return self.get_map(self.curMap)

    def get_currentmap(self):
        return self.get_map(self.curMap)
