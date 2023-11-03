class UndefinedObj:
    """object to be used as a placeholder when None is a valid value."""

    def __repr__(self):
        return "<undefined>"


Undefined = UndefinedObj()

# Power pows ID to color map taken from the documentation (not from the game files)
# https://cattailsgame.com/Cattails%202%20Documentation/doc.html#power_paw_indices
POWER_POWS = (
    {f"Power Paw {n}": "Power Paw Red" for n in range(1, 12)}
    | {f"Power Paw {n}": "Power Paw Yellow" for n in range(12, 15)}
    | {f"Power Paw {n}": "Power Paw Green" for n in range(15, 18)}
    | {f"Power Paw {n}": "Power Paw Blue" for n in range(18, 23)}
    | {f"Power Paw {n}": "Power Paw Purple" for n in range(23, 26)}
    | {f"Power Paw {n}": "Power Paw Rainbow" for n in range(26, 27)}
)
