from enum import Enum


class Category(Enum):
    """
    Enumeration for equipment categories as defined in the PANDA file format.
    """
    LIGHTING = 1
    COMPUTER_AND_COMMUNICATION = 2
    ENTERTAINMENT = 3
    OTHER_APPLIANCES = 4
    GENERATION = 5
    ELECTRIC_VEHICLES = 6
