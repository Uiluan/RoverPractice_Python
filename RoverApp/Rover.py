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

    # TODO: Can I utilize arrays for this? They will autowrap when reaching boundries
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

    def __TurnLeft(self):
        if(self.direction == const.NORTH):
            self.direction = const.WEST
        else:
            self.direction -= 1

    def __TurnRight(self):
        if(self.direction == const.WEST):
            self.direction = const.NORTH
        else:
            self.direction += 1

    def __IsMoveCommand(self, command: str) -> bool:
        return (command.upper() == const.MOVE_COMMAND)

    def __IsLeftCommand(self, command: str) -> bool:
        return (command.upper() == const.LEFT_COMMAND)

    def __IsRightCommand(self, command: str) -> bool:
        return (command.upper() == const.RIGHT_COMMAND)

    def ExecuteCommand(self, command: str) -> str:
        if self.__IsMoveCommand(command):
            if(self.direction == const.NORTH):
                self.__MoveNorth()
            elif(self.direction == const.EAST):
                self.__MoveEast()
            elif(self.direction == const.SOUTH):
                self.__MoveSouth()
            elif(self.direction == const.WEST):
                self.__MoveWest()
        elif(self.__IsLeftCommand(command)):
            self.__TurnLeft()
        elif(self.__IsRightCommand(command)):
            self.__TurnRight()
        
        return str(self.x) + ":" + str(self.y) + ":" + self.__GetDirectionString()