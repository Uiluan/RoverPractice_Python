import pytest
import random
import RoverApp.Constants as const
from RoverApp.Rover import Rover

def test_ExecuteCommand_StartAt_55N_Given_M_EndsAt_56N():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("M")
    expected = "5:6:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55E_Given_M_EndsAt_65N():
    rover = Rover(5, 5, const.EAST)
    actual = rover.ExecuteCommand("M")
    expected = "6:5:E"
    assert actual == expected

def test_ExecuteCommand_StartAt_55S_Given_M_EndsAt_54S():
    rover = Rover(5, 5, const.SOUTH)
    actual = rover.ExecuteCommand("M")
    expected = "5:4:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_M_EndsAt_45W():
    rover = Rover(5, 5, const.WEST)
    actual = rover.ExecuteCommand("M")
    expected = "4:5:W"
    assert actual == expected

def test_ExecuteCommand_StartAt_00S_Given_M_EndsAt_09S():
    rover = Rover(0, 0, const.SOUTH)
    actual = rover.ExecuteCommand("M")
    expected = "0:9:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_09N_Given_M_EndsAt_00N():
    rover = Rover(0, 9, const.NORTH)
    actual = rover.ExecuteCommand("M")
    expected = "0:0:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_00W_Given_M_EndsAt_90W():
    rover = Rover(0, 0, const.WEST)
    actual = rover.ExecuteCommand("M")
    expected = "9:0:W"
    assert actual == expected

def test_ExecuteCommand_StartAt_90E_Given_M_EndsAt_00E():
    rover = Rover(9, 0, const.EAST)
    actual = rover.ExecuteCommand("M")
    expected = "0:0:E"
    assert actual == expected
