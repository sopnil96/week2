"""Tests for Week 2 Harbor Rescue Inventory."""
from src.challenges import (
    mission_snapshot,
    cargo_window,
    first_supply_index,
    supply_report,
    priority_load,
)

def test_mission_snapshot_normal():
    assert mission_snapshot([1, 2, 3]) == (1, 3)

def test_mission_snapshot_empty():
    assert mission_snapshot([]) == (None, None)

def test_mission_snapshot_one_item():
    assert mission_snapshot([42]) == (42, 42)

def test_cargo_window_normal():
    assert cargo_window([1, 2, 3, 4, 5], 1, 3) == [2, 3, 4]

def test_cargo_window_empty_size_zero():
    assert cargo_window([1, 2, 3], 0, 0) == []

def test_cargo_window_out_of_range():
    assert cargo_window([1, 2, 3], 10, 2) == []

def test_cargo_window_past_end():
    assert cargo_window([1, 2, 3], 2, 10) == [3]

def test_first_supply_index_found():
    assert first_supply_index([1, 2, 3], 2) == 1

def test_first_supply_index_not_found():
    assert first_supply_index([1, 2, 3], 9) == -1

def test_supply_report_normal():
    assert supply_report([1, 2, 1, 3], 1) == (2, 0)

def test_supply_report_not_found():
    assert supply_report([1, 2, 3], 9) == (0, -1)

def test_priority_load_normal():
    result = priority_load([1, 2, 3], 0)
    assert result == [0, 1, 2, 3]

def test_priority_load_no_mutation():
    original = [1, 2, 3]
    priority_load(original, 0)
    assert original == [1, 2, 3]
