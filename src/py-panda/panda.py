from typing import Sequence

import numpy as np


class PandaFile:
    """
    A class to represent a PANDA file format. For Documentation see: https://panda.et.tu-dresden.de/
    """
    ALLOWED_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-._:|<>?!$%&=()[]{}\/@‘*0123456789 ")

    MAX_LENGTHS = {
        'lab_id': 4,  # Lab ID is a 4 digit number
        'user_id': 4,  # User ID is a 1 to 4 digit number
        'category': 1,  # Category is a 1 digit number
        'sub_category': 2,  # Sub category is a 1 or 2 digit number
        'sell_year': 4,  # Sell year is a 4 digit number
        'unique_id': 24,  # Unique ID has a maximum of 24 characters
        'manufacturer': 64,  # Manufacturer has a maximum of 64 characters
        'product_code': 64,  # Product code has a maximum of 64 characters
        'sell_country': 2,  # Sell country is a 2-letter code
        'description': 500,  # Description has a maximum of 500 characters

    }

    def __init__(self, lab_id: str, user_id: str, category: int, sub_category: int, unique_id: str, manufacturer: str,
                 product_code: str, sell_country: str, sell_year: str, rated_power: float, nominal_frequency: float,
                 nominal_voltage: float, supply_source: int, description: str, current_harmonics: str,
                 voltage_harmonics: str, sample_rate: int = None, current_data: list[float] = None,
                 voltage_data: list[float] = None):
        """
        Initialize the PANDA file format with the required properties.
        The initialization will validate the lengths and allowed characters for each property.
        EUT = Equipment Under Test

        Args:
        lab_id (str): Laboratory identification number (4 digits).
        user_id (str): User identification number (1 to 4 digits).
        category (int): Category of the equipment (1 digit).
        sub_category (int): Subcategory of the equipment (1 or 2 digits).
        unique_id (str): Unique identification code or number for each EUT (max 24 characters).
        manufacturer (str): Name of the manufacturer (max 64 characters).
        product_code (str): Unique code identifying the EUT (max 64 characters).
        sell_country (str): 2-letter country code where the EUT was bought.
        sell_year (str): Year when the EUT was bought (4 digits).
        rated_power (float): Rated power in W/VA or 'NA' if not available.
        nominal_frequency (float): Nominal frequency in Hz.
        nominal_voltage (float): Nominal voltage in V.
        supply_source (int): Type of source used for measurement (1 digit).
        description (str): Description of the EUT (max 500 characters).
        current_harmonics (str): Current harmonics data.
        voltage_harmonics (str): Voltage harmonics data.
        sample_rate (int, optional): Sampling rate in Samples/s. Required if waveforms are provided.
        current_data (list, optional): Current waveform data. Required if waveforms are provided.
        voltage_data (list, optional): Voltage waveform data. Required if waveforms are provided.
        """
        self.lab_id = self._validate_property('lab_id', lab_id, digits_only=True)
        self.user_id = self._validate_property('user_id', user_id, digits_only=True)
        self.category = self._validate_property('category', str(category), digits_only=True)
        self.sub_category = self._validate_property('sub_category', str(sub_category), digits_only=True)
        self.unique_id = self._validate_property('unique_id', unique_id)
        self.manufacturer = self._validate_property('manufacturer', manufacturer)
        self.product_code = self._validate_property('product_code', product_code)
        self.sell_country = self._validate_property('sell_country', sell_country)
        self.sell_year = self._validate_property('sell_year', sell_year, digits_only=True)
        self.rated_power = rated_power
        self.nominal_frequency = nominal_frequency
        self.nominal_voltage = nominal_voltage
        self.supply_source = supply_source
        self.description = self._validate_property('description', description)
        self.current_harmonics = current_harmonics
        self.voltage_harmonics = voltage_harmonics
        self.sample_rate = sample_rate
        self.current_data = current_data
        self.voltage_data = voltage_data

    @classmethod
    def _validate_property(cls, property_name, value, digits_only=False):
        """
        Validate the length and allowed characters for a given property.

        Args:
        property_name (str): The name of the property to validate.
        value (str): The value of the property.
        digits_only (bool): If True, only digits are allowed in the value.

        Returns:
        str: The validated value.

        Raises:
        ValueError: If the value exceeds the maximum length or contains disallowed characters.
        """
        if digits_only and not value.isdigit():
            raise ValueError(f"{property_name} must contain only digits.")
        if any(char not in cls.ALLOWED_CHARS for char in value):
            raise ValueError(f"Disallowed characters found in {property_name}.")
        if len(value) > cls.MAX_LENGTHS[property_name]:
            raise ValueError(f"{property_name} exceeds maximum length of {cls.MAX_LENGTHS[property_name]} characters.")
        return value

    def to_txt(self, file_path):
        """
        Convert the PANDA file data to a .txt file format.

        Args:
        file_path (str): Path to the .txt file to be created.
        """
        with open(file_path, 'w') as file:
            file.write("TUDHDB_TXT_v01\n")
            file.write("[User Detail]\n")
            file.write(f"Lab_ID = {self.lab_id};\n")
            file.write(f"User_ID = {self.user_id};\n")
            file.write("[EUT]\n")
            file.write(f"Category = {self.category};\n")
            file.write(f"Sub_Category = {self.sub_category};\n")
            file.write(f"Unique_ID = {self.unique_id};\n")
            file.write(f"Manufacturer = {self.manufacturer};\n")
            file.write(f"Product_code = {self.product_code};\n")
            file.write(f"Sell_Country = {self.sell_country};\n")
            file.write(f"Sell_Year = {self.sell_year};\n")
            file.write(f"Rated_Power = {self.rated_power};\n")
            file.write(f"Nominal_Frequency = {self.nominal_frequency};\n")
            file.write(f"Nominal_Voltage = {self.nominal_voltage};\n")
            file.write(f"Supply_Source = {self.supply_source};\n")
            file.write(f"Description = {self.description};\n")
            file.write("[Harmonics]\n")
            file.write(f"Current_Harmonics = {self.current_harmonics};\n")
            file.write(f"Voltage_Harmonics = {self.voltage_harmonics};\n")
            if self.sample_rate is not None:
                file.write("[Waveforms]\n")
                file.write(f"Sampling_Rate = {self.sample_rate};\n")
                file.write(f"Current_Data = {','.join(map(str, self.current_data))};\n")
                file.write(f"Voltage_Data = {','.join(map(str, self.voltage_data))};\n")

    @classmethod
    def from_txt(cls, file_path):
        """
        Create a PANDA file object from a .txt file.

        Args:
        file_path (str): Path to the .txt file to be read.

        Returns:
        PandaFile: An instance of PandaFile with data read from the file.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extracting data from lines
        data = {}
        section = None
        for line in lines:
            if line.strip().endswith(']'):
                section = line.strip().strip('[]')
                data[section] = {}
            elif '=' in line:
                key, value = line.split('=')
                data[section][key.strip()] = value.split(';')[0].strip()

        # Creating a PandaFile object
        return cls(
            lab_id=data['User Detail']['Lab_ID'],
            user_id=data['User Detail']['User_ID'],
            category=int(data['EUT']['Category']),
            sub_category=int(data['EUT']['Sub_Category']),
            unique_id=data['EUT']['Unique_ID'],
            manufacturer=data['EUT']['Manufacturer'],
            product_code=data['EUT']['Product_code'],
            sell_country=data['EUT']['Sell_Country'],
            sell_year=data['EUT']['Sell_Year'],
            rated_power=data['EUT']['Rated_Power'],
            nominal_frequency=float(data['EUT']['Nominal_Frequency']),
            nominal_voltage=int(data['EUT']['Nominal_Voltage']),
            supply_source=int(data['EUT']['Supply_Source']),
            description=data['EUT']['Description'],
            current_harmonics=data['Harmonics']['Current_Harmonics'],
            voltage_harmonics=data['Harmonics']['Voltage_Harmonics'],
            sample_rate=int(data['Waveforms']['Sampling_Rate']) if 'Waveforms' in data else None,
            current_data=[float(i) for i in
                          data['Waveforms']['Current_Data'].split(',')] if 'Waveforms' in data else None,
            voltage_data=[float(i) for i in
                          data['Waveforms']['Voltage_Data'].split(',')] if 'Waveforms' in data else None
        )

    @staticmethod
    def spectrum_to_string(harmonic_orders: Sequence[int | float], magnitudes_rms: Sequence[float],
                           phase_angle_degree: Sequence[float]):
        """
        Convert a harmonic spectrum to a string in the PANDA file format.

        Args:
        harmonic_orders (list): List of harmonic orders.
        magnitudes_rms (list): List of RMS magnitudes.
        phase_angle_degree (list): List of phase angles in degrees.

        Returns:
        str: The harmonic spectrum as a string in the PANDA file format.
        """
        if len(harmonic_orders) != len(magnitudes_rms) or len(harmonic_orders) != len(phase_angle_degree):
            raise ValueError("Length of harmonics, magnitudes and phases must be equal.")
        # Value pairs with a magnitude of zero, which means below the accuracy limit of the
        # measurement system, can be excluded. If value pairs with magnitude of zero are
        # included, the phase angle should be zero as well.
        # Use list comprehension to filter the elements
        filtered_harmonic_orders, filtered_magnitudes_rms, filtered_phase_angle_degree = zip(
            *[(h, m, p) for h, m, p in zip(harmonic_orders, magnitudes_rms, phase_angle_degree) if not np.isclose(m, 0)]
        )

        # Convert the tuples back to lists if necessary
        filtered_harmonic_orders = list(filtered_harmonic_orders)
        filtered_magnitudes_rms = list(filtered_magnitudes_rms)
        filtered_phase_angle_degree = list(filtered_phase_angle_degree)

        spectrum_string = ''
        for harmonic_order, magnitude_rms, phase_angle in zip(filtered_harmonic_orders, filtered_magnitudes_rms,
                                                              filtered_phase_angle_degree):
            spectrum_string += f'{harmonic_order},{magnitude_rms},{phase_angle}/'
        spectrum_string = spectrum_string[:-1]  # Remove trailing slash
        return spectrum_string

    @staticmethod
    def string_to_spectrum(harmonic_string: str):
        """
        Convert a harmonic spectrum string in the PANDA file format to harmonic orders, magnitudes and phase angles.

        Args:
        harmonic_string (str): The harmonic spectrum as a string in the PANDA file format.

        Returns:
        list: List of harmonic orders.
        list: List of RMS magnitudes.
        list: List of phase angles in degrees.
        """
        harmonic_orders = []
        magnitudes_rms = []
        phase_angles = []
        # remove last character if it is a trailing slash
        if harmonic_string.endswith('/'):
            harmonic_string = harmonic_string[:-1]
        for harmonic in harmonic_string.split('/'):
            harmonic_order, magnitude_rms, phase_angle = harmonic.split(',')
            harmonic_orders.append(float(harmonic_order))
            magnitudes_rms.append(float(magnitude_rms))
            phase_angles.append(float(phase_angle))
        return harmonic_orders, magnitudes_rms, phase_angles


if __name__ == '__main__':
    import configparser
    import os

    config = configparser.ConfigParser()
    config.sections()
    config_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    config.read(os.path.join(config_path, 'config.ini'))
    data_path = os.path.abspath(os.path.join(config_path, os.path.expanduser(config['DEFAULT']['data_path'])))
    test_file = "Charging with max. current (16 A).txt"
    test_file_path = os.path.join(data_path, test_file)
    panda_file = PandaFile.from_txt(test_file_path)
    current_harmonics = PandaFile.string_to_spectrum(panda_file.current_harmonics)
    voltage_harmonics = PandaFile.string_to_spectrum(panda_file.voltage_harmonics)
    pass
