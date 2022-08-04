import RoverApp.Constants as const

class Rover():
    def __init__(self, x: int=const.X_MIN, y:int=const.Y_MIN, direction:int=const.NORTH) -> None:
        self.y = y
        self.x = x
        self.direction = direction

    def ExecuteCommand(self, command: str) -> str:
        if(command == const.MOVE_COMMAND):
            if(self.direction == const.NORTH):
                self.y += 1
            elif(self.direction == const.EAST):
                self.x += 1
        
        return str(self.x) + ":" + str(self.y) + ":" + self.__GetDirectionString()

    def __GetDirectionString(self):
        if(self.direction == const.NORTH):
            return "N"
        elif(self.direction == const.EAST):
            return "E"