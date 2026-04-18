[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TeyGQAqr)

# Week 2: Harbor Rescue Inventory

## Summary
The Harbor Rescue Inventory assignment provides a set of utility functions
to manage cargo data stored in Python lists. It focuses on list manipulation,
searching, slicing, and index tracking. These tools simulate an inventory
system where we need to quickly identify mission boundaries, extract specific
cargo windows, locate supply items, and generate reports on inventory counts.

## Approach

### `mission_snapshot`
- Checks if the list is empty and returns `(None, None)` immediately.
- Otherwise uses direct index access `items[0]` and `items[-1]` to return
the first and last items in constant time.

### `cargo_window`
- Validates `start` and `size` parameters first, returning `[]` for any
invalid input.
- Uses Python slicing `items[start : start + size]` to return the range.

### `first_supply_index`
- Uses `enumerate` to loop through the list once.
- Returns the index immediately on the first match.
- Returns -1 if the loop completes without finding the target.

### `supply_report`
- Performs a single linear pass over the list.
- Tracks both count and the first index encountered.
- Returns `(0, -1)` if the target does not appear.

### `priority_load` *(stretch)*
- Uses list concatenation `[urgent_item] + items` to create a brand-new
list, ensuring the original input list remains unchanged.

## Complexity

| Function | Time | Space | Why |
| :--- | :--- | :--- | :--- |
| mission_snapshot | O(1) | O(1) | Direct index access |
| cargo_window | O(k) | O(k) | Slice of size k |
| first_supply_index | O(n) | O(1) | Single pass |
| supply_report | O(n) | O(1) | Single pass |
| priority_load | O(n) | O(n) | Copies the list |

## Edge-case checklist
- [x] empty list
- [x] one-item list
- [x] target missing
- [x] repeated values
- [x] slice goes past end
- [x] size is zero
- [x] size is negative
- [x] original list unchanged in priority_load

## Assistance & Sources
- Python Documentation: syntax reference for list slicing and `enumerate`
- AI use: Yes — AI helped review implemented functions and this README