from deus.generator.terrain import GenTerrain

class World():
    def __init__(self):
        self.genTerrain = GenTerrain()

    def GenerateTerrain(self):
        self.terrain = self.genTerrain.Generate()

    def TerrainGetValue(self, row, col):
        return self.terrain[row][col]

    def TerrainGetBytes(self):
        result = []
        for row in self.terrain:
            result += row

        return bytes(result)
