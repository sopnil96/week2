"""Week 2 starter code for Harbor Rescue Inventory."""
from __future__ import annotations


def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    """Return the first and last items in the list.
    Return (None, None) if the list is empty.
    """
    if not items:
        return (None, None)
    return (items[0], items[-1])


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    """Return up to ``size`` items starting at index ``start``.
    Return an empty list if ``start`` is out of range or if ``size <= 0``.
    """
    if size <= 0 or start < 0 or start >= len(items):
        return []
    return items[start : start + size]


def first_supply_index(items: list[object], target: object) -> int:
    """Return the index of the first occurrence of ``target``.
    Return -1 if the target is not found.
    """
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    """Return (count, first_index) for ``target`` in ``items``.
    Return (0, -1) if the target does not appear.
    """
    count = 0
    first_index = -1
    for index, item in enumerate(items):
        if item == target:
            if first_index == -1:
                first_index = index
            count += 1
    return (count, first_index)


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    """Return a new list with ``urgent_item`` added at the front.
    Do not mutate the original input list.
    """
    return [urgent_item] + items