import tile
import portal
import portalExit
import json
import key

class Board:

    def __init__(self, filename):

        # open the json file and store it into levelData
        try:
            with open(filename) as f:
                self.levelData = json.load(f)
        except IOError as e:
            print("Couldn't open json file (%s)." % e)

        # board has height, width, tile size, player starting position, and probably an array of enemy starting positions

        self.height = self.levelData["height"]
        self.width = self.levelData["width"]
        self.size = self.levelData["tileSize"]
        self.playerPosition = (self.levelData["player"][1], self.levelData["player"][0]) # player starting position as (x, y) tuple
        self.exitKeysRequired = self.levelData["exit"]["keys"]
        self.keys = list()
        self.makeBoard()

    def makeBoard(self):

        # board should be [x][y]
        self.tiles = [[tile.Tile("empty") for y in range(self.height)] for x in range(self.width)]

        # populate static objects: walls, lava, and exit

        for wall in self.levelData["walls"]:
            x = wall["position"][0]
            y = wall["position"][1]
            self.tiles[x][y].type = "wall"

        for deathTile in self.levelData["deathTiles"]:
            x = deathTile["position"][0]
            y = deathTile["position"][1]
            self.tiles[x][y].type = "lava"

        exitX = self.levelData["exit"]["position"][0]
        exitY = self.levelData["exit"]["position"][1]

        self.tiles[exitX][exitY].type = "exit"

        # Need to figure out how wormholes will be stored

        for wormhole in self.levelData["wormholes"]:
            entranceX = wormhole["positionEntrance"][0]
            entranceY = wormhole["positionEntrance"][1]
            exitX = wormhole["positionExit"][0]
            exitY = wormhole["positionExit"][1]
            entranceDirection = wormhole["directionEntrance"]
            exitDirection = wormhole["directionExit"]

            self.tiles[exitX][exitY] = portalExit.PortalExit(exitDirection)
            self.tiles[entranceX][entranceY] = portal.Portal(entranceDirection, self.tiles[exitX][exitY])
            self.tiles[entranceX][entranceY].exitX = exitX
            self.tiles[entranceX][entranceY].exitY = exitY

        # populate keys

        for keyObj in self.levelData["keys"]:
            x = keyObj["startingPosition"][0]
            y = keyObj["startingPosition"][1]
            xmin = keyObj["positionBoundsX"][0]
            xmax = keyObj["positionBoundsX"][1]
            ymin = keyObj["positionBoundsY"][0]
            ymax = keyObj["positionBoundsY"][1]
            self.tiles[x][y].key = True
            self.keys.append(key.Key(x, y, xmin, xmax, ymin, ymax))
