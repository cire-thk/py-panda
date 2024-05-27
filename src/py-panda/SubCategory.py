from enum import Enum


class SubCategory(Enum):
    """
    Enumeration for equipment subcategories as defined in the PANDA file format.
    """
    # Lighting Subcategories
    INCANDESCENT_FILAMENT_LAMP = (1, 1)
    COMPACT_FLUORESCENT_LAMP = (1, 2)
    FLUORESCENT_LAMP_ELECTRONIC = (1, 3)
    FLUORESCENT_LAMP_NON_ELECTRONIC = (1, 4)
    INTEGRATED_SOLID_STATE_LAMP = (1, 5)
    NON_INTEGRATED_SOLID_STATE_LAMP = (1, 6)
    LIGHTING_OTHER = (1, 7)

    # Computer and Communication Subcategories
    DESKTOP = (2, 1)
    LAPTOP = (2, 2)
    MOBILE_DEVICE = (2, 3)
    MONITOR = (2, 4)
    PRINTER_SCANNER_MULTIFUNCTIONAL = (2, 5)
    NETWORK_EQUIPMENT = (2, 6)
    STORAGE = (2, 7)
    PERMANENT_CONNECTED_PHONES = (2, 8)
    COMPUTER_OTHER_CHARGING = (2, 9)
    COMPUTER_OTHER_NONCHARGING = (2, 10)

    # Entertainment Subcategories
    CRT_TELEVISION_SET = (3, 1)
    FLAT_PANEL_TELEVISION_SET = (3, 2)
    PROJECTORS = (3, 3)
    AUDIO_VIDEO_PHOTO_CHARGING = (3, 4)
    AUDIO_VIDEO_PHOTO_NONCHARGING = (3, 5)
    GAME_CONSOLE_CHARGING = (3, 6)
    GAME_CONSOLE_NONCHARGING = (3, 7)
    ENTERTAINMENT_OTHER_CHARGING = (3, 8)
    ENTERTAINMENT_OTHER_NONCHARGING = (3, 9)

    # Other Appliances Subcategories
    KITCHEN = (4, 1)
    LAUNDRY = (4, 2)
    BATHROOM = (4, 3)
    OFFICE = (4, 4)
    TOOLS_AND_GARDEN = (4, 5)
    BATTERY_CHARGERS = (4, 6)
    OTHER = (4, 7)

    # Generation Subcategories
    PHOTOVOLTAIC_SYSTEM = (5, 1)
    MICRO_CHP = (5, 2)
    SMALL_WIND_ELECTRIC_SYSTEM = (5, 3)
    GENERATION_OTHER = (5, 4)

    # Electric Vehicles Subcategories
    ELECTRIC_CAR = (6, 1)
    ELECTRIC_BIKE = (6, 2)
    ELECTRIC_MOTORCYCLE_AND_SCOOTERS = (6, 3)
    CHARGING_STATION_WITH_INTEGRATED_RECTIFIER = (6, 4)
    ELECTRIC_VEHICLES_OTHER = (6, 5)
