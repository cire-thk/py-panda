from enum import Enum


class SupplySource(Enum):
    """
    Enumeration for supply sources as defined in the PANDA file format.
    In the context of PANDA, LF phenomena cover all frequencies below 40th
    harmonic, where spectrum information is available.
    HF phenomena cover all frequencies higher than the 40th harmonic and
    require the storage of raw waveform data
    """
    GRID_VOLTAGE = 1
    PROGRAMMABLE_GENERATOR_SINUSOIDAL = 2
    PROGRAMMABLE_GENERATOR_NONSINUSOIDAL_LF_HARMONICS = 3
    PROGRAMMABLE_GENERATOR_NONSINUSOIDAL_HF_HARMONICS = 4
    PROGRAMMABLE_GENERATOR_NONSINUSOIDAL_LF_HF_HARMONICS = 5
