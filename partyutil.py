"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if name and email are related to Mel.

    >>> is_mel('hi', 'hi')
    False

    >>> is_mel('hi', 'mel@ubermelon.com')
    True

    >>> is_mel('Mel Melitpolski', 'hi')
    True

    >>> is_mel('Mel Melitpolski', 'mel@ubermelon.com')
    True

    >>> is_mel('Hi', 'MEL@UBERMELON.COM')
    True

    >>> is_mel('Mel Isbeingsneaky', 'hi')
    True

    >>> is_mel('Whome? Melitpolski', 'hi')
    True
    """
    return ('mel' in name.lower()
            or 'melitpolski' in name.lower() 
            or email.lower() == 'mel@ubermelon.com')

    # return name == 'Mel Melitpolski' or email == 'mel@ubermelon.com'


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.

    >>> treats = [{'type': 'dessert'},{'type': 'dessert'},{'type': 'appetizer'},\
    {'type': 'dessert'},{'type': 'appetizer'},{'type': 'drink'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'drink')

    >>> treats = [{'type': 'dessert'},{'type': 'drink'},{'type': 'appetizer'},\
    {'type': 'dessert'},{'type': 'appetizer'},{'type': 'drink'}]
    >>> most_and_least_common_type(treats)
    ('appetizer', 'appetizer')

    >>> treats = [{'type': 'dessert'},{'type': 'dessert'},{'type': 'appetizer'},\
    {'type': 'dessert'},{'type': 'appetizer'},{'type': 'drink'},\
    {'type': 'appetizer'}]
    >>> most_and_least_common_type(treats)
    ('appetizer', 'drink')

    >>> treats = []
    >>> most_and_least_common_type(treats)
    (None, None)

    >>> treats = [{'type': 'dessert'}]
    >>> most_and_least_common_type(treats)
    ('dessert', 'dessert')
    """

    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
