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

def test_ExecuteCommand_StartAt_55N_Given_m_EndsAt_56N():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("m")
    expected = "5:6:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55N_Given_L_EndsAt_55W():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("L")
    expected = "5:5:W"
    assert actual == expected

def test_ExecuteCommand_StartAt_55N_Given_l_EndsAt_55W():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("l")
    expected = "5:5:W"
    assert actual == expected

def test_ExecuteCommand_StartAt_55E_Given_L_EndsAt_55N():
    rover = Rover(5, 5, const.EAST)
    actual = rover.ExecuteCommand("L")
    expected = "5:5:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55E_Given_l_EndsAt_55N():
    rover = Rover(5, 5, const.EAST)
    actual = rover.ExecuteCommand("l")
    expected = "5:5:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55S_Given_L_EndsAt_55E():
    rover = Rover(5, 5, const.SOUTH)
    actual = rover.ExecuteCommand("L")
    expected = "5:5:E"
    assert actual == expected

def test_ExecuteCommand_StartAt_55S_Given_l_EndsAt_55E():
    rover = Rover(5, 5, const.SOUTH)
    actual = rover.ExecuteCommand("l")
    expected = "5:5:E"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_L_EndsAt_55S():
    rover = Rover(5, 5, const.WEST)
    actual = rover.ExecuteCommand("L")
    expected = "5:5:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_l_EndsAt_55S():
    rover = Rover(5, 5, const.WEST)
    actual = rover.ExecuteCommand("l")
    expected = "5:5:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_R_EndsAt_55N():
    rover = Rover(5, 5, const.WEST)
    actual = rover.ExecuteCommand("R")
    expected = "5:5:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_r_EndsAt_55N():
    rover = Rover(5, 5, const.WEST)
    actual = rover.ExecuteCommand("r")
    expected = "5:5:N"
    assert actual == expected

def test_ExecuteCommand_StartAt_55N_Given_R_EndsAt_55E():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("R")
    expected = "5:5:E"
    assert actual == expected

def test_ExecuteCommand_StartAt_55N_Given_r_EndsAt_55E():
    rover = Rover(5, 5, const.NORTH)
    actual = rover.ExecuteCommand("r")
    expected = "5:5:E"
    assert actual == expected

def test_ExecuteCommand_StartAt_55E_Given_R_EndsAt_55S():
    rover = Rover(5, 5, const.EAST)
    actual = rover.ExecuteCommand("R")
    expected = "5:5:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_55W_Given_r_EndsAt_55S():
    rover = Rover(5, 5, const.EAST)
    actual = rover.ExecuteCommand("r")
    expected = "5:5:S"
    assert actual == expected

def test_ExecuteCommand_StartAt_55S_Given_R_EndsAt_55W():
    rover = Rover(5, 5, const.SOUTH)
    actual = rover.ExecuteCommand("R")
    expected = "5:5:W"
    assert actual == expected

def test_ExecuteCommand_StartAt_55S_Given_r_EndsAt_55W():
    rover = Rover(5, 5, const.SOUTH)
    actual = rover.ExecuteCommand("r")
    expected = "5:5:W"
    assert actual == expected