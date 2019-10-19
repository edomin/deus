import random

class GenTerrain():
    def __init__(self):
        pass

    def FillOldValues(self, newTerrain):
        for row in range(0, self.side):
            for col in range(0, self.side):
                newTerrain[row * 2][col * 2] = self.terrain[row][col]

    def GetRandomDiff(self, diff):
        return random.randrange(-diff, diff, 1)

    def FillBorder(self, newTerrain, newSide, diff):
        for i in range(0, newSide - 2, 2):
            newTerrain[0][i + 1] = (
             (newTerrain[0][i] + newTerrain[0][i + 2]) / 2
              + self.GetRandomDiff(diff)
             )
            newTerrain[newSide - 1][i + 1] = (
             newTerrain[newSide - 1][i] + newTerrain[newSide - 1][i + 2]
            ) / 2 + self.GetRandomDiff(diff)
            newTerrain[i + 1][0] = (
             (newTerrain[i][0] + newTerrain[i + 2][0]) / 2
             + self.GetRandomDiff(diff)
            )
            newTerrain[i + 1][newSide - 1] = (
             newTerrain[i][newSide - 1] + newTerrain[i + 2][newSide - 1]
            ) / 2 + self.GetRandomDiff(diff)

    def FillBody(self, newTerrain, newSide, diff):
        for row in range(1, newSide - 1, 2):
            for col in range(1, newSide - 1, 2):
                newTerrain[row][col] = (
                 newTerrain[row - 1][col - 1] + newTerrain[row - 1][col + 1]
                 + newTerrain[row + 1][col - 1] + newTerrain[row + 1][col + 1]
                ) / 4 + self.GetRandomDiff(diff)

        if newSide >= 5:
            for row in range(1, newSide - 1):
                if row % 2 == 1:
                    colRangeLeft = 2
                    colRangeRight = newSide - 2
                else:
                    colRangeLeft = 1
                    colRangeRight = newSide - 1
                for col in range(colRangeLeft, colRangeRight, 2):
                    newTerrain[row][col] = (
                     newTerrain[row][col - 1] + newTerrain[row][col + 1]
                     + newTerrain[row - 1][col] + newTerrain[row + 1][col]
                    ) / 4 + self.GetRandomDiff(diff);

    def CompleteIteration(self):
        newSide = self.side * 2 - 1
        newIteration = self.iteration + 1
        diff = 73 - newIteration * 8
        newTerrain = []
        for i in range(0, newSide):
            newTerrain.append([0] * newSide)
        self.FillOldValues(newTerrain)
        self.FillBorder(newTerrain, newSide, diff)
        self.FillBody(newTerrain, newSide, diff)
        self.terrain = newTerrain
        self.iteration = newIteration
        self.side = newSide

    def RoundValues(self):
        for row in range(0, self.side):
            for col in range(0, self.side):
                self.terrain[row][col] = int(self.terrain[row][col])

    def ShapeLimitHeights(self):
        for row in range(0, self.side):
            for col in range(0, self.side):
                if self.terrain[row][col] < 0:
                    self.terrain[row][col] = 0;
                if self.terrain[row][col] > 255:
                    self.terrain[row][col] = 255;

    def Smooth(self):
        smoothed = []
        for i in range(0, self.side):
            smoothed.append([0] * self.side)
        for row in range(1, self.side - 1):
            for col in range(1, self.side - 1):
                smoothed[row][col] = (
                 self.terrain[row - 1][col - 1] + self.terrain[row - 1][col]
                  + self.terrain[row - 1][col + 1] + self.terrain[row][col - 1]
                  + self.terrain[row][col] + self.terrain[row][col + 1]
                  + self.terrain[row + 1][col - 1] + self.terrain[row + 1][col]
                  + self.terrain[row + 1][col + 1]
                ) / 9

        self.terrain = smoothed

    def Generate(self):
        self.terrain = [[127, 127], [127, 127]]
        self.iteration = 0
        self.side = 2

        self.CompleteIteration() #3
        self.CompleteIteration() #5
        self.CompleteIteration() #9
        self.CompleteIteration() #17
        self.CompleteIteration() #33
        self.CompleteIteration() #65
        self.CompleteIteration() #129
        self.CompleteIteration() #257
        self.CompleteIteration() #513

        #self.Smooth()
        #self.Smooth()
        #self.Smooth()
        #self.Smooth()
        #self.Smooth()

        #self.Smooth()
        #self.Smooth()
        #self.Smooth()
        #self.Smooth()
        #self.Smooth()

        self.RoundValues()

        self.ShapeLimitHeights()

        return self.terrain
