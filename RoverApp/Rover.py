import RoverApp.Constants as const

class Rover():
    def __init__(self, x: int=const.X_MIN, y:int=const.Y_MIN, direction:int=const.NORTH) -> None:
        self._y = y
        self._x = x
        self._direction = direction

    def __GetDirectionString(self):
        return {
            const.NORTH: "N",
            const.EAST: "E",
            const.SOUTH: "S",
            const.WEST: "W"
        } [self._direction]

    # TODO: Can I utilize arrays for this? They will autowrap when reaching boundries
    def __MoveNorth(self):
        if(self._y == const.Y_MAX):
            self._y = const.Y_MIN
        else:
            self._y += 1

    def __MoveEast(self):
        if(self._x == const.Y_MAX):
            self._x = const.Y_MIN
        else:
            self._x += 1

    def __MoveSouth(self):
        if(self._y == const.Y_MIN):
            self._y = const.Y_MAX
        else:
            self._y -= 1

    def __MoveWest(self):
        if(self._x == const.X_MIN):
            self._x = const.Y_MAX
        else:
            self._x -= 1

    def __TurnLeft(self):
        if(self._direction == const.NORTH):
            self._direction = const.WEST
        else:
            self._direction -= 1

    def __TurnRight(self):
        if(self._direction == const.WEST):
            self._direction = const.NORTH
        else:
            self._direction += 1

    def __IsMoveCommand(self, command: str) -> bool:
        return (command.upper() == const.MOVE_COMMAND)

    def __IsLeftCommand(self, command: str) -> bool:
        return (command.upper() == const.LEFT_COMMAND)

    def __IsRightCommand(self, command: str) -> bool:
        return (command.upper() == const.RIGHT_COMMAND)

    def __ExecuteIndividualCommand(self, command: str):
        if self.__IsMoveCommand(command):
            if(self._direction == const.NORTH):
                self.__MoveNorth()
            elif(self._direction == const.EAST):
                self.__MoveEast()
            elif(self._direction == const.SOUTH):
                self.__MoveSouth()
            elif(self._direction == const.WEST):
                self.__MoveWest()
        elif(self.__IsLeftCommand(command)):
            self.__TurnLeft()
        elif(self.__IsRightCommand(command)):
            self.__TurnRight()

    def ExecuteCommand(self, command: str) -> str:
        for char in command:
            self.__ExecuteIndividualCommand(char)
        
        return str(self._x) + ":" + str(self._y) + ":" + self.__GetDirectionString()