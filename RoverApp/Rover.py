import RoverApp.Constants as const

class Rover():
    def __init__(self, x: int=const.X_MIN, y:int=const.Y_MIN, direction:int=const.NORTH) -> None:
        self.y = y
        self.x = x
        self.direction = direction

    def __GetDirectionString(self):
        return {
            const.NORTH: "N",
            const.EAST: "E",
            const.SOUTH: "S",
            const.WEST: "W"
        } [self.direction]

    def __MoveNorth(self):
        if(self.y == const.Y_MAX):
            self.y = const.Y_MIN
        else:
            self.y += 1

    def __MoveEast(self):
        if(self.x == const.Y_MAX):
            self.x = const.Y_MIN
        else:
            self.x += 1

    def __MoveSouth(self):
        if(self.y == const.Y_MIN):
            self.y = const.Y_MAX
        else:
            self.y -= 1

    def __MoveWest(self):
        if(self.x == const.X_MIN):
            self.x = const.Y_MAX
        else:
            self.x -= 1

    def ExecuteCommand(self, command: str) -> str:
        if(command == const.MOVE_COMMAND):
            if(self.direction == const.NORTH):
                self.__MoveNorth()
            elif(self.direction == const.EAST):
                self.__MoveEast()
            elif(self.direction == const.SOUTH):
                self.__MoveSouth()
            elif(self.direction == const.WEST):
                self.__MoveWest()
        
        return str(self.x) + ":" + str(self.y) + ":" + self.__GetDirectionString()