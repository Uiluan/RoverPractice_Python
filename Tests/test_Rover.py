import pytest
import random
import RoverApp.Constants as const
from RoverApp.Rover import Rover

def test_ExecuteCommand_StartAt_00N_Given_M_EndsAt_01N():
    rover = Rover(0, 0, const.NORTH)

    actual = rover.ExecuteCommand("M")
    expected = "0:1:N"
    assert actual == expected, f"Expected: {expected}, got: {actual}"

def test_ExecuteCommand_StartAt_00E_Given_M_EndsAt_10N():
    rover = Rover(0, 0, const.EAST)

    actual = rover.ExecuteCommand("M")
    expected = "1:0:E"
    assert actual == expected, f"Expected: {expected}, got: {actual}"