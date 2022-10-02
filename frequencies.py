"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    if items is None:
        return frequencies

    for item in items:
        sitem = str(item)
        if sitem in frequencies:
            frequencies[sitem] += 1
        else:
            frequencies[sitem] = 1

    return frequencies
